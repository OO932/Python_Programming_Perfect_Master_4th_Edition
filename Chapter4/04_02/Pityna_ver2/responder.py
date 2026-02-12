import random

class responder(object):
    """ 応答クラスのスーパークラス
    """

    def __init__ (seslf, name):
        """ Responderオブジェクトの名前をnameに格納
        Args:
            name (str): Responderオブジェクトの名前     
        """
        self.name = name

    