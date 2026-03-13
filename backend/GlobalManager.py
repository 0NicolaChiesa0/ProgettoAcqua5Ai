class ChoiceEnum(str, _Enum):
    ALL_TO_A = "all to a"
    ALL_TO_B = "all to b"
    SHARED   = "shared"



class GlobalManager:
    INSTANCE: GlobalManager

    def __init__(self):
        GlobalManager.INSTANCE = self

        self.choice: ChoiceEnum = None