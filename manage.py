from flask_script import Manager, Server
from app import create_app

app = create_app()
manager = Manager(app)

print "--- CONFIG: ", app.config.get('CONFIG')
print "--- AMQP:", app.config.get('NAMEKO_AMQP_URI')
print "--- DEBUG:", app.config.get('DEBUG')

manager.add_command('runserver', Server(
    host=app.config.get('SERVER_ADDRESS'),
    port=app.config.get('PORT'),
    use_reloader=True)
                    )

if __name__ == '__main__':
    manager.run()
