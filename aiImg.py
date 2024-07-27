from stability_sdk import client
from PIL import Image
import io
import warnings
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
key = "sk-sFnZLnSIpcPB9LZrz4dgVj9p30v0mOlJHu7g60OhBiRBkcLR"


class AIImg():
    def __init__(self):
        pass

    def genrateImg(self, text):
        self.text = text
        """Enter text that you want to see as a image"""

        stability_api = client.StabilityInference(
            key=key,
            verbose=True

        )
        answers = stability_api.generate(
            prompt=self.text,
            seed=34567,
            steps=5


        )
        for resp in answers:
            for artifact in resp.artifacts:  # type: ignore
                if artifact.finish_reason == generation.FILTER:
                    warnings.warn("Some thing is wrong")

                if artifact.type == generation.ARTIFACT_IMAGE:
                    img2 = Image.open(io.BytesIO(artifact.binary))
                    img2.save("./static/img/aiImg.jpg")
                    return True

        return False
