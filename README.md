# Example of Python 3 setters and getters using properties with inheritance

Output:

```
$ python3 set_get.py 
INFO Superclass data can be changed from the subclass, new value appears everywhere:
INFO main: Creating a new LambdaConfig, which creates a new BaseConfig
INFO BaseConfig.__init__: set self.base_data = '{'aws_lambda': {'dir': 'old_value'}}'
INFO BaseConfig: self.data getter returning = '{'aws_lambda': {'dir': 'old_value'}}'
INFO main: aws_lambda_data = {'dir': 'old_value'}
INFO BaseConfig: self.data getter returning = '{'aws_lambda': {'dir': 'old_value'}}'
INFO LambdaConfig: dir setter before setting to first_new_value is 'old_value'
INFO LambdaConfig.dir setter after set: base_data['dir'] = 'first_new_value'
INFO main: after setting lambda_config.dir='first_new_value', aws_lambda_data['dir'] = first_new_value
INFO main: aws_lambda_data = {'dir': 'first_new_value'}
INFO main: aws_lambda_data['dir'] = first_new_value
```
