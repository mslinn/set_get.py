import logging


class BaseConfig:

    def __init__(self, diktionary):
        self.base_data = diktionary

    @property
    def data(self) -> dict:
        logging.debug(f"BaseConfig: Getting data = {self.base_data}")
        return self.base_data

    @data.setter
    def data(self, value):
        logging.debug(f"BaseConfig: Setting data to {value}")
        self.base_data = value

    def change_property_value(self, name, new_value):
        x = self.base_data
        self.base_data[name] = new_value


class LambdaConfig(BaseConfig):

    def __init__(self, diktionary):
        super().__init__(diktionary)

    @property
    def data(self):
        return super().data
    
    @data.setter
    def data(self, new_value):
        super(LambdaConfig, type(self))._data.fset(self, new_value)
        
    @property
    def dir(self):
        result = self.data['dir']
        logging.debug(f"LambdaConfig: Getting dir = {result}")
        return result

    @dir.setter
    def dir(self, new_value):
        base_data = super(LambdaConfig, type(self)).data.fget(self)
        #logging.debug(f"LambdaConfig.dir.setter: base_data = {base_data}")
        logging.debug(f"LambdaConfig: dir before setting to {new_value} is {base_data['aws_lambda']['dir']}")
        base_data['aws_lambda']['dir'] = new_value
        #logging.debug(f"LambdaConfig.dir.setter after set: base_data = {base_data}")
        logging.debug(f"LambdaConfig.dir.setter after set: base_data['dir'] = {base_data['aws_lambda']['dir']}")


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
    base_config = BaseConfig(diktionary)
    logging.info(f"main: base_config.data = {base_config.data}")

    lambda_data = base_config.data['aws_lambda']
    logging.info(f"main: lambda_data = {lambda_data}")
    logging.info(f"main: lambda_data['dir'] = {lambda_data['dir']}")
    logging.info("")

    logging.info("Superclass data can be changed from the superclass, new value appears everywhere:")
    base_config.data['aws_lambda']["dir"] = "first_new_value"
    logging.info(f"main: base_config.data['aws_lambda']['dir'] (#1) = {base_config.data['aws_lambda']['dir']}")
    logging.info(f"main: lambda_data['dir'] (#1) = {lambda_data['dir']}")
    logging.info("")

    logging.info("Superclass data can be changed from the subclass, new value appears everywhere:")
    logging.info("main: Creating a new LambdaConfig, which creates a new BaseConfig")
    lambda_config = LambdaConfig(diktionary)
    lambda_config.dir = "second_new_value"
    logging.info(f"main: lambda_data['dir'] = {lambda_data['dir']}")
    logging.info(f"main: base_config.data['aws_lambda']['dir'] (#2) = {base_config.data['aws_lambda']['dir']}")

