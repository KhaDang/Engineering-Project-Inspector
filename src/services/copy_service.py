import os
import shutil
from pathlib import Path

from models.copy_request import CopyRequest, CopyResult

# Import Exception
from exceptions.base_exception import EmptyFolderError

class CopyService:

    def copy(
        self,
        indexed_files,
        request: CopyRequest,
        progress_message=None
            ):

        result = CopyResult(
            copied=[],
            skipped=[],
            duplicates=[],
            failed=[]
        )


        if not os.path.isdir(request.destination):
            raise EmptyFolderError(request.destination)

        destination_path = Path(request.destination)
        destination_path.mkdir(
            parents=True,
            exist_ok=True
        )
        if progress_message:
            progress_total_count = 0
            for drawing in request.lookup_list:
                if indexed_files.get(drawing):
                    progress_total_count += 1
            progress_message.start_progress(progress_total_count)

        current = 0
        for drawing in request.lookup_list:
            drawing_files = indexed_files.get(drawing)
            if not drawing_files:
                continue

            if drawing_files:
                current += 1
                if progress_message:
                    progress_message.update_progress(current, drawing)

            for extension in request.extensions:
                files = drawing_files.get_path(extension)
                # if not files:
                #     continue
                #
                # if len(files) > 1:
                #
                #     result.duplicates.append(
                #         f"{drawing}{extension}"
                #     )
                #
                #     continue
                if files:
                    source = Path(files)

                    print(f'source: {source}')

                    destination = (
                        destination_path /
                        source.name
                    )

                    try:

                        shutil.copy2(
                            source,
                            destination
                        )

                        result.copied.append(
                            destination
                        )

                    except OSError as error:

                        result.failed.append(
                            f"{source}: {error}"
                        )
        return result

