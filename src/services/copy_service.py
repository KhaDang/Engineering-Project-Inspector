
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

        request.destination.mkdir(
            parents=True,
            exist_ok=True
        )

        for drawing in request.lookup_list:

            drawing_files = indexed_files.get(drawing)

            if not drawing_files:
                continue

            for extension in request.extensions:

                files = drawing_files.get(
                    extension,
                    []
                )

                if len(files) == 0:
                    continue

                if len(files) > 1:

                    result.duplicates.append(
                        f"{drawing}{extension}"
                    )

                    continue

                source = Path(files[0])

                destination = (
                    request.destination /
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

