import logging


class BaseConfig:

    def __init__(self, diktionary):
        self.base_data = diktionary
        logging.info(f"BaseConfig.__init__: set self.base_data = '{self.base_data}'")

    @property
    def data(self) -> dict:
        logging.info(f"BaseConfig: self.data getter returning = '{self.base_data}'")
        return self.base_data

    @data.setter
    def data(self, value):
        logging.info(f"BaseConfig: self.data setter, new value for self.base_data='{value}'")
        self.base_data = value


class LambdaConfig(BaseConfig):

    def __init__(self, diktionary):
        super().__init__(diktionary)
        self.base_data = super(LambdaConfig, type(self)).data.fget(self)

    @property
    def data(self):
        return super().data
    
    @data.setter
    def data(self, new_value):
        super(LambdaConfig, type(self))._data.fset(self, new_value)
        
    @property
    def dir(self):
        result = self.data['dir']
        logging.info(f"LambdaConfig: Getting dir = '{result}'")
        return result

    @dir.setter
    def dir(self, new_value):
        #logging.debug(f"LambdaConfig.dir.setter: base_data = {base_data}")
        logging.info(f"LambdaConfig: dir setter before setting to {new_value} is '{self.base_data['aws_lambda']['dir']}'")
        self.base_data['aws_lambda']['dir'] = new_value
        #logging.debug(f"LambdaConfig.dir.setter after set: base_data = {base_data}")
        logging.info(f"LambdaConfig.dir setter after set: self.base_data['dir'] = '{self.base_data['aws_lambda']['dir']}'")


if __name__ == "__main__":
    logging.basicConfig(
        format = '%(levelname)s %(message)s',
        level = logging.INFO
    )
    
    diktionary = { 
        "aws_lambda": {
            "dir": "old_value"
        }
    }

    logging.info("Superclass data can be changed from the subclass, new value appears everywhere:")
    logging.info("main: Creating a new LambdaConfig, which creates a new BaseConfig")
    lambda_config = LambdaConfig(diktionary)
    aws_lambda_data = lambda_config.data['aws_lambda']
    logging.info(f"main: aws_lambda_data = {aws_lambda_data}")
    lambda_config.dir = "first_new_value"
    logging.info(f"main: after setting lambda_config.dir='first_new_value', aws_lambda_data['dir'] = {aws_lambda_data['dir']}")

    logging.info(f"main: aws_lambda_data = {aws_lambda_data}")
    logging.info(f"main: aws_lambda_data['dir'] = '{aws_lambda_data['dir']}'")

