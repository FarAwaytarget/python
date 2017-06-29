import pygal

wm = pygal.Worldmap()
wm.title = 'population of countries in North America'
wm.add('North America', {'ca':3412600, 'us':309349000, 'mx':113423000})
wm.add('china',{'cn':60203123} )
wm.render_to_file('na_population.svg')