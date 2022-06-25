import traceback
import typing
from support.Slack.BaseSlack import BaseSlack
from support.paragraph.ParagraphDTO import ParagraphDTO


class ParagraphSaveFailed(BaseSlack):

    def __init__(self,exception_error) -> None:
        self.exception_error = exception_error
        super().__init__()

    def create_notification(self)-> typing.Dict[str, str]:
        return {
            "error":''.join(traceback.format_exception(etype=type(self.exception_error), value=self.exception_error, tb=self.exception_error.__traceback__))
            }