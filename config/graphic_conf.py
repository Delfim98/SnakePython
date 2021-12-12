import configparser


class GraphicConfig(object):
    windowWidth:int = 400
    windowHeight:int = 400
    windowCaption:str = ""
    backgroundColor = (255,255,255)
    cellBorderSize:int = 4
    cellBorderColor = (255,255,255)
    snakeColor = (255,255,255)
    fruitColor = (255,255,255)
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read('resources/config.cfg')
        graphicConfig = config['graphic']
        self.windowWidth = int(graphicConfig['windowWidth'])
        self.windowHeight = int(graphicConfig['windowHeight'])
        self.windowCaption = graphicConfig['windowCaption']
        self.cellBorderSize = int(graphicConfig['cellBorderSize'])
        self.cellBorderColor = [int(c) for c in graphicConfig['cellBorderColor'].split(',')]
        self.backgroundColor = [int(c) for c in graphicConfig['backgroundColor'].split(',')]
        self.snakeColor = [int(c) for c in graphicConfig['snakeColor'].split(',')]
        self.fruitColor = [int(c) for c in graphicConfig['fruitColor'].split(',')]