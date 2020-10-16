import logging


class BaseConfig:
    """ See https://stackoverflow.com/q/64389885/553865 """

    def __init__(self, _dictionary):
        self._base_data = _dictionary
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

    # Start of boilerplate

    def __init__(self, _dictionary):
        super().__init__(_dictionary)

    @property
    def lambda_data(self):
        return self.data['aws_lambda']

    @lambda_data.setter
    def lambda_data(self, new_value):
        data = self.data
        data['aws_lambda'] = new_value
        self.data = data  # Trigger the super() data.setter, which saves to a file

    def generalized_setter(self, key, new_value):
        lambda_data = self.lambda_data
        lambda_data[key] = new_value
        # Python's call by value means the super().data setter is called, which modifies super().base_data:
        self.lambda_data = lambda_data

    # End of boilerplate. Properties specific to this class follow:

    @property
    def dir(self):
        result = self.data['dir']
        return result

    @dir.setter
    def dir(self, new_value):
        self.generalized_setter("dir", new_value)


    @property
    def name(self):
        return self.data['name']

    @name.setter
    def name(self, new_value):
        self.generalized_setter("name", new_value)


    @property
    def id(self):
        return self.data['id']

    @id.setter
    def id(self, new_value):
        self.generalized_setter("id", new_value)


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
        },
        "more_keys": {
            "key1": "old_value1",
            "key2": "old_value2"
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
    logging.info("")

    lambda_config.id = "new_id"
    logging.info(f"main: after setting lambda_config.id='new_id', aws_lambda_data['id'] = {aws_lambda_data['id']}")
    logging.info(f"main: aws_lambda_data = {aws_lambda_data}")
    logging.info(f"main: aws_lambda_data['id'] = '{aws_lambda_data['id']}'")
    logging.info("")

    logging.info(f"main: lambda_config.data = {lambda_config.data}")
