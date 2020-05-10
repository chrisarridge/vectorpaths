import numpy as np
import matplotlib.pyplot as plt
import logging

import paths

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Construct points along Archimedian spiral.
t = np.linspace(0,30,100)
r = 0 + 0.1*t
xc = r*np.cos(t)
yc = r*np.sin(t)
plt.plot(xc, yc, 'o')

# Fit bezier curves with a maximum error of 0.25.
beziers = paths.fit_cubic_bezier(xc, yc, 0.25)
print('Accuracy of 0.25 requires {} bezier patches'.format(len(beziers)))
[b.plot(color='r') for b in beziers]

# Fit bezier curves with a maximum error of 0.05.
beziers = paths.fit_cubic_bezier(xc, yc, 0.05)
print('Accuracy of 0.05 requires {} bezier patches'.format(len(beziers)))
[b.plot(color='b') for b in beziers]

plt.show()
