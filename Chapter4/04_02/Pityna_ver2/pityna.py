import responder

class Pityna(object):
    """ ピティナの本体クラス
    """
    def __inint__(self, name):
        """ インスタンス変数name､rsponderの初期化

        Args:
            name (str): Pitynaの名前
        """
        # Pitynaオブジェクトの名前をインスタンス変数に代入
        self.name = name
        # Responderオブジェクトをインスタンス変数に代入
        self.responder = responder.RandomResponder('Random')

    def daialogue(self, input):
        """ 応答オブジェクトのresponse()を呼び出して応答文字列を取得する

        Args:
            input (str): ユーザー発言
        Returns:
            str: 応答メッセージ
        """
        return self.responder.response(input)

    def get_responder_name(self):
        """ 応答に使用されたオブジェクト名を返す
    　　Args:
            self(object): 呼び出し元のPitynaオブジェクト
       Returns:
            str: 応答オブジェクト名
        """
        # responderに格納されているオブジェクト名を返す
        return self.responder.name
    
    def get_name(self):
        """ Pitynaオブジェクトの名前を返す
    　　Args:
            self(object): 呼び出し元のPitynaオブジェクト
       Returns:
            str: Pitynaクラスの名前
        """
        # Pitynaクラスの名前を返す
        return self.name
    