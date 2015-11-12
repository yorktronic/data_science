import numpy as np
import statsmodels.formula.api as smf

# Set seet for reproducible results
np.random.seed(414)

# Generate toy data
X = np.linspace(0, 15, 1000)
Y = 3 * np.sin(X) + np.random.normal(1 + X, 0.2, 1000)

TRAIN_X, TRAIN_Y = X[:700], Y[:700]
TEST_X, TEST_Y = X[700:], Y[700:]

TRAIN_DF = pd.DataFrame({'X': TRAIN_X, 'Y', TRAIN_Y})
TEST_DF = pd.DataFrame({'X': TEST_X, 'Y', TEST_Y})

# Linear fit
POLY1 = smf.ols(formula = 'Y ~ 1 + X', data=TRAIN_DF).fit()

# Quadratic fit
POLY2 = smf.ols(formula = 'Y ~ 1 + X + I(X**2)', data=TRAIN_DF).fit()
