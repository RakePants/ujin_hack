class ConsumerAuth:
    def __init__(self, con_token: str) -> None:
        self.con_token: str = con_token
        self.entity_guid_type: int = 7