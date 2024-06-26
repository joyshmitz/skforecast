# Unit test predict_quantiles ForecasterAutoregMultiVariate
# ==============================================================================
import numpy as np
import pandas as pd
from skforecast.ForecasterAutoregMultiVariate import ForecasterAutoregMultiVariate
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

# Fixtures
from .fixtures_ForecasterAutoregMultiVariate import series
from .fixtures_ForecasterAutoregMultiVariate import exog
from .fixtures_ForecasterAutoregMultiVariate import exog_predict

transformer_exog = ColumnTransformer(
                       [('scale', StandardScaler(), ['exog_1']),
                        ('onehot', OneHotEncoder(), ['exog_2'])],
                       remainder = 'passthrough',
                       verbose_feature_names_out = False
                   )


def test_predict_quantiles_output_when_forecaster_is_LinearRegression_steps_is_2_in_sample_residuals_True_exog_and_transformer():
    """
    Test output of predict_quantiles when regressor is LinearRegression,
    2 steps are predicted, using in-sample residuals, exog is included and both
    inputs are transformed.
    """
    forecaster = ForecasterAutoregMultiVariate(
                     regressor          = LinearRegression(),
                     steps              = 2,
                     level              = 'l1',
                     lags               = 3,
                     transformer_series = StandardScaler(),
                     transformer_exog   = transformer_exog
                 )
    
    forecaster.fit(series=series, exog=exog)
    results = forecaster.predict_quantiles(
                  steps               = 2,
                  exog                = exog_predict,
                  quantiles           = [0.05, 0.55, 0.95],
                  n_boot              = 4,
                  in_sample_residuals = True
              )
    
    expected = pd.DataFrame(
                   data    = np.array([[0.39855187, 0.56310088, 0.67329092],
                                       [0.17729748, 0.48969677, 0.81780586]]),
                   columns = ['l1_q_0.05', 'l1_q_0.55', 'l1_q_0.95'],
                   index   = pd.RangeIndex(start=50, stop=52)
               )
    
    pd.testing.assert_frame_equal(expected, results)


def test_predict_quantiles_output_when_forecaster_is_LinearRegression_steps_is_2_in_sample_residuals_False_exog_and_transformer():
    """
    Test output of predict_quantiles when regressor is LinearRegression,
    2 steps are predicted, using out-sample residuals, exog is included and both
    inputs are transformed.
    """
    forecaster = ForecasterAutoregMultiVariate(
                     regressor          = LinearRegression(),
                     steps              = 2,
                     level              = 'l1',
                     lags               = 3,
                     transformer_series = StandardScaler(),
                     transformer_exog   = transformer_exog
                 )
    
    forecaster.fit(series=series, exog=exog)
    forecaster.out_sample_residuals = forecaster.in_sample_residuals
    results = forecaster.predict_quantiles(
                  steps               = 2,
                  exog                = exog_predict,
                  quantiles           = [0.05, 0.55, 0.95],
                  n_boot              = 4,
                  in_sample_residuals = False
              )
    
    expected = pd.DataFrame(
                   data    = np.array([[0.39855187, 0.56310088, 0.67329092],
                                       [0.17729748, 0.48969677, 0.81780586]]),
                   columns = ['l1_q_0.05', 'l1_q_0.55', 'l1_q_0.95'],
                   index   = pd.RangeIndex(start=50, stop=52)
               )

    pd.testing.assert_frame_equal(expected, results)