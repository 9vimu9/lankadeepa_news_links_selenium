from abc import ABC, abstractmethod
import typing
import urllib3
import json
import traceback


from support.Constant import Constant


class BaseSlack(ABC):

    @abstractmethod
    def create_notification(self)-> typing.Dict[str, str]:
        pass



    def send(self):
        try:
            message_data = "{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in self.create_notification().items()) + "}"


            urllib3.PoolManager().request('POST',
                                    Constant.SLACK_WEB_HOOK_URL,
                                    body = json.dumps({
                                        'text': message_data
                                        }),
                                    headers = {'Content-Type': 'application/json'},
                                    retries = True)
        except:
            traceback.print_exc()

        return True
