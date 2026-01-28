class Pityna:
    """ ピティナの本体クラス
    """
    def __init__(self, name):
        """ インスタンス変数name､responderの初期化

        Args:
            name (str): Pitynaオブジェクトの名前
        """
        # Pitynaオブジェクトの名前をインスタンス変数に代入
        self.name = name
        # Responderオブジェクトを生成してインスタンス変数に代入
        self.responder = Responder('Repeat')
        