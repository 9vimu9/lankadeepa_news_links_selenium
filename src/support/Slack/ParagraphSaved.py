import typing
from support.Slack.BaseSlack import BaseSlack
from support.paragraph.ParagraphDTO import ParagraphDTO


class ParagraphSaved(BaseSlack):

    def __init__(self,paragraphDTO:ParagraphDTO) -> None:
        self.paragraphDTO = paragraphDTO
        super().__init__()

    def create_notification(self)-> typing.Dict[str, str]:
        return self.paragraphDTO.dic()