# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

""" Greeting """


def greet(name, greetings='Hello, <name>!'):
    new_greeting = greetings.replace('<name>', name)
    print(new_greeting)
    return new_greeting


""" Force """


def force(mass, body='earth'):
    planets = {
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "earth": 9.798,
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58,
    }
    planet_gravity = planets[body]
    planet_gravity_round = round(planet_gravity, 1)
    force_calc = (float(mass) * planet_gravity_round)
    print("force is: ", force_calc, "N")
    return (force_calc)


""" Gravity """


def pull(m1, m2, d):
    gravity_constant = 6.674 * (10**-11)
    force_newton = (gravity_constant * m1 * m2) / (d**2)
    print("gravitational force is: ", force_newton, "of N")
    return (force_newton)


""" Greeting """
name = 'Bob'
greetings = 'Hello, <name>!'
greet(name, greetings)

""" Force """
mass = 1
body = 'earth'
force(mass, body)

""" Gravity """
m1 = 800
m2 = 1500
d = 3
pull(m1, m2, d)
