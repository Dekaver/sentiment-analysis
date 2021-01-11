import twint #configuration


config = twint.Config()
config.Search = "Vaksin covid"
config.Since = '2020-12-1 00:00:00'
config.Until = '2020-12-8 00:00:00'
config.Store_json = True
config.Lang = "in"
config.Hide_output = True
config.Filter_retweets = True
config.Output = "data/vaksinTWEET.json"
twint.run.Search(config)
