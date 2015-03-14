from demo_app import app

app.config.from_object('demo_app.configmodule.DevelopmentConfig')
print " * " + app.config.get('CONFIG_VARIANTE') + "-Modus"
app.run(app.config.get('HOST'), app.config.get('PORT'), app.config.get('DEBUG'))