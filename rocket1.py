from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.00002)
rocket = Rocket(earth, altitude=408365, velocity=7645, timezoom=3)
earth.run(rocket)
