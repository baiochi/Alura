
class UrlExtractor():

    def __init__(self, url) -> None:
        self.url = url
        self.url_integrity()
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self) -> str:
        return self.url + '\nBase url:' + self.get_base_url() + '\nParameters:' + str(self.get_url_params())
    
    def __eq__(self, __o: object) -> bool:
        return self.url == __o.url

    def url_integrity(self):
        if self.url:
            self.url = self.url.strip() # clear white spaces in the beggining
        else:
            raise ValueError('Empty URL')
    
    def get_base_url(self):

        param_begin_index = self.url.find('?')

        return self.url[:param_begin_index]

    def get_url_params(self):

        param_begin_index = self.url.find('?')
        full_params = self.url[param_begin_index+1:]

        return {key:value for (key,value) in [param.split('=') for param in full_params.split('&')]} 