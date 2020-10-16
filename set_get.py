import logging


class BaseConfig:

    def __init__(self, diktionary):
        self._base_data = diktionary
        logging.info(f"BaseConfig.__init__: set self.base_data = '{self._base_data}'")

    def save_data(self):
        logging.info(f"BaseConfig: Pretending to save self.base_data='{self._base_data}'")

    @property
    def data(self) -> dict:
        logging.info(f"BaseConfig: self.data getter returning = '{self._base_data}'")
        return self._base_data

    @data.setter
    def data(self, value):
        logging.info(f"BaseConfig: self.data setter, new value for self.base_data='{value}'")
        self._base_data = value
        self.save_data()


class LambdaConfig(BaseConfig):
    """ This example subclass is one of several imaginary subclasses, all with similar structures.
    Each subclass only works with data within a portion of super().data;
    for example, this subclass only looks at and modifies data within super().data['aws_lambda'].
    """

    def __init__(self, diktionary):
        super().__init__(diktionary)
        # See https://stackoverflow.com/a/10810545/553865:
        self.base_data_property = super(LambdaConfig, type(self)).data
        # This subclass only modifies data contained within self.lambda_data:
        self.lambda_data = super().data['aws_lambda']

    @property
    def lambda_data(self):
        return self.base_data_property.fget(self)['aws_lambda']

    @lambda_data.setter
    def lambda_data(self, new_value):
        super().data['aws_lambda'] = new_value
        self.base_data_property.fset(self, super().data)

    # Properties specific to this class follow

    @property
    def dir(self):
        result = self.data['dir']
        logging.info(f"LambdaConfig: Getting dir = '{result}'")
        return result

    @dir.setter
    def dir(self, new_value):
        logging.info(f"LambdaConfig: dir setter before setting to {new_value} is '{self.lambda_data['dir']}'")
        # Python's call by value means super().data is called, which modifies super().base_data:
        self.lambda_data['dir'] = new_value
        self.base_data_property.fset(self, super().data)  # This no-op merely triggers super().@data.setter
        logging.info(f"LambdaConfig.dir setter after set: self.lambda_data['dir'] = '{self.lambda_data['dir']}'")


    @property
    def name(self):  # Comments are as for the dir property
        return self.data['name']

    @name.setter
    def name(self, new_value):  # Comments are as for the dir property
        self.lambda_data['name'] = new_value
        self.base_data_property.fset(self, super().data)


    @property
    def id(self):  # Comments are as for the dir property
        return self.data['id']

    @id.setter
    def id(self, new_value):  # Comments are as for the dir property
        self.lambda_data['id'] = new_value
        self.base_data_property.fset(self, super().data)


if __name__ == "__main__":
    logging.basicConfig(
        format = '%(levelname)s %(message)s',
        level = logging.INFO
    )

    diktionary = {
        "aws_lambda": {
            "dir": "old_dir",
            "name": "old_name",
            "id": "old_id"
        }
    }

    logging.info("Superclass data can be changed from the subclass, new value appears everywhere:")
    logging.info("main: Creating a new LambdaConfig, which creates a new BaseConfig")
    lambda_config = LambdaConfig(diktionary)
    aws_lambda_data = lambda_config.data['aws_lambda']
    logging.info(f"main: aws_lambda_data = {aws_lambda_data}")
    logging.info("")

    lambda_config.dir = "new_dir"
    logging.info(f"main: after setting lambda_config.dir='new_dir', aws_lambda_data['dir'] = {aws_lambda_data['dir']}")
    logging.info(f"main: aws_lambda_data = {aws_lambda_data}")
    logging.info(f"main: aws_lambda_data['dir'] = '{aws_lambda_data['dir']}'")
    logging.info("")

    lambda_config.name = "new_name"
    logging.info(f"main: after setting lambda_config.name='new_name', aws_lambda_data['name'] = {aws_lambda_data['name']}")
    logging.info(f"main: aws_lambda_data = {aws_lambda_data}")
    logging.info(f"main: aws_lambda_data['name'] = '{aws_lambda_data['name']}'")

    lambda_config.id = "new_id"
    logging.info(f"main: after setting lambda_config.id='new_id', aws_lambda_data['id'] = {aws_lambda_data['id']}")
    logging.info(f"main: aws_lambda_data = {aws_lambda_data}")
    logging.info(f"main: aws_lambda_data['id'] = '{aws_lambda_data['id']}'")
