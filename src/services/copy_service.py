import shutil
from pathlib import Path

from models.copy_request import CopyRequest, CopyResult

class CopyService:

    def copy(
        self,
        indexed_files,
        request: CopyRequest
            ):

        result = CopyResult(
            copied=[],
            skipped=[],
            duplicates=[],
            failed=[]
        )

        destination_path = Path(request.destination)
        destination_path.mkdir(
            parents=True,
            exist_ok=True
        )

        for drawing in request.lookup_list:
            drawing_files = indexed_files.get(drawing)

            if not drawing_files:
                continue
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

