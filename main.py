# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting_template='Hello, <name>!'):
    greeting = greeting_template.replace('<name>', name)
    print(greeting)


greet('bob')


def force(mass, body='earth'):
    bodies = {
        'sun': 274,
        'jupiter': 24.92,
        'neptune': 11.15,
        'saturn': 10.44,
        'earth': 9.798,
        'uranus': 8.87,
        'venus': 8.87,
        'mars': 3.71,
        'mercury': 3.7,
        'moon': 1.62,
        'pluto': 0.58
    }
    gravity = round(bodies[body], 1)
    answer = mass * gravity
    print(
        f"the gravity from an object is {mass} kg on the planet {body} it's {answer} Newton")


force(3.4, 'moon')


def pull(m1: float, m2: float, d: float):
    gravity = 6.674 * 10 ** (-11)
    pull = gravity * (m1 * m2) / d ** 2
    print(pull)


pull(0.1, 5.972*10**24, 6.371*10**6)
