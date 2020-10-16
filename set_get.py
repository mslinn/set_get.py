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
        self.base_data_property = super(LambdaConfig, type(self)).data
        self.lambda_data = self.base_data['aws_lambda']

    @property
    def data(self):
        return super().data
    
    @data.setter
    def data(self, new_value):
        self.base_data_property.fset(self, new_value)
        
    # Properties specific to this class follow
        
    @property
    def dir(self):
        result = self.data['dir']
        logging.info(f"LambdaConfig: Getting dir = '{result}'")
        return result

    @dir.setter
    def dir(self, new_value):
        logging.info(f"LambdaConfig: dir setter before setting to {new_value} is '{self.lambda_data['dir']}'")
        self.lambda_data['dir'] = new_value
        logging.info(f"LambdaConfig.dir setter after set: self.base_data['dir'] = '{self.lambda_data['dir']}'")


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

