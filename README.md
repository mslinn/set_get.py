# Example of Python 3 setters and getters using properties with inheritance

Output:

```
$ python3 set_get.py 
INFO main: base_config.data = {'aws_lambda': {'dir': 'old_value'}}
INFO main: lambda_data = {'dir': 'old_value'}
INFO main: lambda_data['dir'] = old_value
INFO 
INFO Superclass data can be changed from the superclass, new value appears everywhere:
INFO main: base_config.data['aws_lambda']['dir'] (#1) = first_new_value
INFO main: lambda_data['dir'] (#1) = first_new_value
INFO 
INFO Superclass data can be changed from the subclass, new value appears everywhere:
INFO main: Creating a new LambdaConfig, which creates a new BaseConfig
INFO main: lambda_data['dir'] = second_new_value
INFO main: base_config.data['aws_lambda']['dir'] (#2) = second_new_value
```
