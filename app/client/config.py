from src.app.auth import ConsumerAuth


class Config:
    def __init__(self, con_token: str, **kwargs) -> None:
        self.auth: ConsumerAuth = ConsumerAuth(con_token)
        
        self.host = kwargs['host']
        self.port = kwargs.get('port')
        if self.port:
            self.host += f':{self.port}'
        self.protocol = kwargs.get('protocol')
        if not self.protocol:
            self.protocol = 'https://'
    



    