<script src="https://kit.fontawesome.com/d20edc211b.js" crossorigin="anonymous"></script>

<img src="img/banner-landing-page-skforecast.png#only-light" align="left"  style="
    margin-bottom: 30px;
    margin-top: 0px;">

<img src="img/banner-landing-page-dark-mode-skforecast-no-background.png#only-dark" align="left" style="
    margin-bottom: 30px;
    margin-top: 0px;">


![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)
[![PyPI](https://img.shields.io/pypi/v/skforecast)](https://pypi.org/project/skforecast/)
[![codecov](https://codecov.io/gh/JoaquinAmatRodrigo/skforecast/branch/master/graph/badge.svg)](https://codecov.io/gh/JoaquinAmatRodrigo/skforecast)
[![Build status](https://github.com/JoaquinAmatRodrigo/skforecast/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/JoaquinAmatRodrigo/skforecast/actions/workflows/unit-tests.yml/badge.svg)
[![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/JoaquinAmatRodrigo/skforecast/graphs/commit-activity)
[![Downloads](https://static.pepy.tech/personalized-badge/skforecast?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/skforecast)
[![License](https://img.shields.io/github/license/JoaquinAmatRodrigo/skforecast)](https://github.com/JoaquinAmatRodrigo/skforecast/blob/master/LICENSE)
[![DOI](https://zenodo.org/badge/337705968.svg)](https://zenodo.org/doi/10.5281/zenodo.8382787)
[![paypal](https://img.shields.io/static/v1?style=social&amp;label=Donate&amp;message=%E2%9D%A4&amp;logo=Paypal&amp;color&amp;link=%3curl%3e)](https://www.paypal.com/donate/?hosted_button_id=D2JZSWRLTZDL6)
[![buymeacoffee](https://img.shields.io/badge/-Buy_me_a%C2%A0coffee-gray?logo=buy-me-a-coffee)](https://www.buymeacoffee.com/skforecast)
![GitHub Sponsors](https://img.shields.io/github/sponsors/joaquinamatrodrigo?logo=github&label=Github%20sponsors&link=https%3A%2F%2Fgithub.com%2Fsponsors%2FJoaquinAmatRodrigo)
[![!slack](https://img.shields.io/static/v1?logo=linkedin&label=LinkedIn&message=news&color=lightblue)](https://www.linkedin.com/company/skforecast/)
[![NumFOCUS Affiliated](https://img.shields.io/badge/NumFOCUS-Affiliated%20Project-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org/sponsored-projects/affiliated-projects)


## About The Project

**Skforecast** is a Python library for time series forecasting using machine learning models. It works with any regressor compatible with the scikit-learn API, including popular options like LightGBM, XGBoost, CatBoost, Keras, and many others.

**Why use skforecast?**

The fields of statistics and machine learning have developed many excellent regression algorithms that can be useful for forecasting, but applying them effectively to time series analysis can still be a challenge. To address this issue, the skforecast library provides a comprehensive set of tools for training, validation and prediction in a variety of scenarios commonly encountered when working with time series. The library is built using the widely used scikit-learn API, making it easy to integrate into existing workflows. With skforecast, users have access to a wide range of functionalities such as feature engineering, model selection, hyperparameter tuning and many others. This allows users to focus on the essential aspects of their projects and leave the intricacies of time series analysis to skforecast. In addition, skforecast is developed according to the following priorities:

+ Fast and robust prototyping. :zap:
+ Validation and backtesting methods to have a realistic assessment of model performance. :mag:
+ Models must be deployed in production. :hammer:
+ Models must be interpretable. :crystal_ball:

**Share Your Thoughts with Us**

Thank you for choosing skforecast! We value your suggestions, bug reports and recommendations as they help us identify areas for improvement and ensure that skforecast meets the needs of the community. Please consider sharing your experiences, reporting bugs, making suggestions or even contributing to the codebase on GitHub. Together, let's make time series forecasting more accessible and accurate for everyone.


## Installation & Dependencies

To install the basic version of `skforecast` with its core dependencies, run:

```bash
pip install skforecast
```

If you want to learn more about the installation process, dependencies and optional features, please refer to the [Installation Guide](https://skforecast.org/latest/quick-start/how-to-install.html).


## Forecasters

A **Forecaster** object in the skforecast library is a comprehensive container that provides essential functionality and methods for training a forecasting model and generating predictions for future points in time.

The **skforecast** library offers a variety of forecaster types, each tailored to specific requirements such as single or multiple time series, direct or recursive strategies, or custom predictors. Regardless of the specific forecaster type, all instances share the same API.

| Forecaster                   | Single series | Multiple series | Recursive strategy | Direct strategy | Probabilistic prediction | Time series differentiation | Exogenous features | Custom features |
|:-----------------------------|:-------------:|:---------------:|:------------------:|:---------------:|:------------------------:|:---------------------------:|:------------------:|:---------------:|
|[ForecasterAutoreg]           |✔️||✔️||✔️|✔️|✔️||
|[ForecasterAutoregCustom]     |✔️||✔️||✔️|✔️|✔️|✔️|✔️|
|[ForecasterAutoregDirect]     |✔️|||✔️|✔️||✔️||
|[ForecasterMultiSeries]       ||✔️|✔️||✔️|✔️|✔️||
|[ForecasterMultiSeriesCustom] ||✔️|✔️||✔️|✔️|✔️|✔️|
|[ForecasterMultiVariate]      ||✔️||✔️|✔️||✔️||
|[ForecasterRNN]               ||✔️||✔️|||||
|[ForecasterSarimax]           |✔️||✔️||✔️|✔️|✔️||

[ForecasterAutoreg]: https://skforecast.org/latest/user_guides/autoregresive-forecaster.html
[ForecasterAutoregCustom]: https://skforecast.org/latest/user_guides/window-features-and-custom-features.html
[ForecasterAutoregDirect]: https://skforecast.org/latest/user_guides/direct-multi-step-forecasting.html
[ForecasterMultiSeries]: https://skforecast.org/latest/user_guides/independent-multi-time-series-forecasting.html
[ForecasterMultiSeriesCustom]: https://skforecast.org/latest/user_guides/window-features-and-custom-features.html#forecasterautoregmultiseriescustom
[ForecasterMultiVariate]: https://skforecast.org/latest/user_guides/dependent-multi-series-multivariate-forecasting.html
[ForecasterRNN]: https://skforecast.org/latest/user_guides/forecasting-with-deep-learning-rnn-lstm
[ForecasterSarimax]: https://skforecast.org/latest/user_guides/forecasting-sarimax-arima.html


## Features

+ Create Forecasters from any regressor that follows the scikit-learn API
+ Include exogenous variables as predictors
+ Include custom predictors (rolling mean, rolling variance ...)
+ Multiple backtesting methods for model validation
+ Grid search, random search and Bayesian search to find optimal lags (predictors) and best hyperparameters
+ Prediction interval estimated by bootstrapping and quantile regression
+ Include custom metrics for model validation and grid search
+ Get predictor importance
+ Forecaster in production


## Examples and tutorials

### English

<i class="fa-duotone fa-chart-line fa" style="font-size: 25px; color:#1DA1F2;"></i>  [**Skforecast: time series forecasting with Machine Learning**](https://www.cienciadedatos.net/documentos/py27-time-series-forecasting-python-scikitlearn.html)

<i class="fa-solid fa-arrow-trend-up" style="color: #E60023;"></i> [**ARIMA and SARIMAX models**](https://www.cienciadedatos.net/documentos/py51-arima-sarimax-models-python.html)

<i class="fa-solid fa-sitemap fa" style="font-size: 25px; color:#00cc99;"></i> [**Forecasting with gradient boosting: XGBoost, LightGBM and CatBoost**](https://www.cienciadedatos.net/documentos/py39-forecasting-time-series-with-skforecast-xgboost-lightgbm-catboost.html)

<i class="fa-solid fa-diagram-project fa-rotate-90" style="font-size: 25px; color:#74C0FC;"></i> [**Forecasting with XGBoost**](https://www.cienciadedatos.net/documentos/py56-forecasting-time-series-with-xgboost.html)

<i class="fa-duotone fa-water fa" style="font-size: 25px; color:teal;"></i> [**Global Forecasting Models: Multi-series forecasting**](https://www.cienciadedatos.net/documentos/py44-multi-series-forecasting-skforecast.html)

<i class="fa-light fa-chart-line fa" style="font-size: 25px; color:#f26e1d;"></i>  [**Probabilistic forecasting models**](https://www.cienciadedatos.net/documentos/py42-probabilistic-forecasting.html)

<i class="fa-solid fa-layer-group" style="color: #001633;"></i> [**Forecasting with Deep Learning**](https://cienciadedatos.net/documentos/py54-forecasting-with-deep-learning)

<i class="fa-solid fa-arrow-trend-up" style="color: #fbbb09;"></i> [**Modelling time series trend with tree based models**](https://www.cienciadedatos.net/documentos/py49-modelling-time-series-trend-with-tree-based-models.html)


<i class="fa-solid fa-chart-gantt" style="color: #ff004f;"></i> [**Interpretable forecasting models**](https://www.cienciadedatos.net/documentos/py57-interpretable-forecasting-models.html)

<i class="fa-solid fa-wave-square" style="color: #fbbb09;"></i> [**Intermittent demand forecasting**](https://www.cienciadedatos.net/documentos/py48-intermittent-demand-forecasting.html)

<i class="fa-solid fa-magnifying-glass" style="font-size: 25px; color:purple;"></i> [**Forecasting time series with missing values**](https://www.cienciadedatos.net/documentos/py46-forecasting-time-series-missing-values.html)

<i class="fa-solid fa-cubes-stacked fa-rotate-180" style="color: #c15d0b;"></i> [**Stacking ensemble of machine learning models to improve forecasting**](https://cienciadedatos.net/documentos/py52-stacking-ensemble-models-forecasting.html)

<i class="fa-duotone fa-lightbulb fa" style="font-size: 25px; color:#fcea2b;"></i> [**Forecasting energy demand with machine learning**](https://www.cienciadedatos.net/documentos/py29-forecasting-electricity-power-demand-python.html)

<i class="fa-solid fa-globe" style="font-size: 25px; color:#6b8e23;"></i> [**Global Forecasting Models: Comparative Analysis of Single and Multi-Series Forecasting Modeling**](https://www.cienciadedatos.net/documentos/py53-global-forecasting-models.html)

<i class="fa-solid fa-virus-covid" style="font-size: 25px; color:red;"></i> [**Mitigating the impact of covid on forecasting models**](https://www.cienciadedatos.net/documentos/py45-weighted-time-series-forecasting.html)

<i class="fa-duotone fa-rss fa" style="font-size: 25px; color:#666666;"></i> [**Forecasting web traffic with machine learning and Python**](https://www.cienciadedatos.net/documentos/py37-forecasting-web-traffic-machine-learning.html)

<i class="fa-brands fa-bitcoin fa" style="font-size: 25px; color:#f7931a;"></i> [**Bitcoin price prediction with Python**](https://www.cienciadedatos.net/documentos/py41-forecasting-cryptocurrency-bitcoin-machine-learning-python.html)



### Español

<i class="fa-duotone fa-chart-line fa" style="font-size: 25px; color:#1DA1F2;"></i> [**Skforecast: forecasting series temporales con Machine Learning**](https://www.cienciadedatos.net/documentos/py27-forecasting-series-temporales-python-scikitlearn.html)

<i class="fa-solid fa-arrow-trend-up" style="color: #E60023;"></i> [**Modelos ARIMA y SARIMAX**](https://cienciadedatos.net/documentos/py51-modelos-arima-sarimax-python.html)

<i class="fa-solid fa-sitemap fa" style="font-size: 25px; color:#00cc99;"></i> [**Forecasting con gradient boosting: XGBoost, LightGBM y CatBoost**](https://www.cienciadedatos.net/documentos/py39-forecasting-series-temporales-con-skforecast-xgboost-lightgbm-catboost.html)

<i class="fa-duotone fa-water fa" style="font-size: 25px; color:teal;"></i> [**Global Forecasting Models: Multi-series forecasting**](https://www.cienciadedatos.net/documentos/py44-multi-series-forecasting-skforecast-español.html)

<i class="fa-light fa-chart-line fa" style="font-size: 25px; color:#f26e1d;"></i>  [**Forecasting probabilístico**](https://www.cienciadedatos.net/documentos/py42-intervalos-prediccion-modelos-forecasting-machine-learning.html)

<i class="fa-solid fa-layer-group" style="color: #001633;"></i> [**Forecasting con Deep Learning**](https://cienciadedatos.net/documentos/py54-forecasting-con-deep-learning)

<i class="fa-solid fa-wave-square" style="color: #fbbb09;"></i> [**Predicción demanda intermitente**](https://www.cienciadedatos.net/documentos/py48-forecasting-demanda-intermitente.html)

<i class="fa-solid fa-arrow-trend-up" style="color: #fbbb09;"></i> [**Modelar series temporales con tendencia utilizando modelos de árboles**](https://cienciadedatos.net/documentos/py49-modelar-tendencia-en-series-temporales-modelos-de-arboles.html)

<i class="fa-duotone fa-lightbulb fa" style="font-size: 25px; color:#fcea2b;"></i> [**Forecasting de la demanda eléctrica**](https://www.cienciadedatos.net/documentos/py29-forecasting-demanda-energia-electrica-python.html)

<i class="fa-duotone fa-rss fa" style="font-size: 25px; color:#666666;"></i>  [**Forecasting de las visitas a una página web**](https://www.cienciadedatos.net/documentos/py37-forecasting-visitas-web-machine-learning.html)

<i class="fa-solid fa-virus-covid" style="font-size: 25px; color:red;"></i> [**Reducir el impacto del Covid en modelos de forecasting**](https://cienciadedatos.net/documentos/py45-weighted-time-series-forecasting-es)

<i class="fa-brands fa-bitcoin fa" style="font-size: 25px; color:#f7931a;"></i> [**Predicción del precio de Bitcoin con Python**](https://www.cienciadedatos.net/documentos/py41-forecasting-criptomoneda-bitcoin-machine-learning-python.html)

<i class="fa-brands fa-youtube" style="font-size: 25px; color:#c4302b;"></i> [**Workshop predicción de series temporales con machine learning 
Universidad de Deusto / Deustuko Unibertsitatea**](https://youtu.be/MlktVhReO0E)


## How to contribute

Primarily, skforecast development consists of adding and creating new *Forecasters*, new validation strategies, or improving the performance of the current code. However, there are many other ways to contribute:

- Submit a bug report or feature request on [GitHub Issues](https://github.com/JoaquinAmatRodrigo/skforecast/issues).
- Contribute a Jupyter notebook to our [examples](https://skforecast.org/latest/examples/examples).
- Write [unit or integration tests](https://docs.pytest.org/en/latest/) for our project.
- Answer questions on our issues, Stack Overflow, and elsewhere.
- Translate our documentation into another language.
- Write a blog post, tweet, or share our project with others.

For more information on how to contribute to skforecast, see our [Contribution Guide](https://github.com/JoaquinAmatRodrigo/skforecast/blob/master/CONTRIBUTING.md).

Visit our [authors section](https://skforecast.org/latest/authors/authors) to meet all the contributors to skforecast.


## Citation

If you use skforecast for a scientific publication, we would appreciate citations to the published software.

**Zenodo**

```
Amat Rodrigo, Joaquin, & Escobar Ortiz, Javier. (2024). skforecast (v0.13.0). Zenodo. https://doi.org/10.5281/zenodo.8382788
```

**APA**:
```
Amat Rodrigo, J., & Escobar Ortiz, J. (2024). skforecast (Version 0.13.0) [Computer software]. https://doi.org/10.5281/zenodo.8382788
```

**BibTeX**:
```
@software{skforecast,
author = {Amat Rodrigo, Joaquin and Escobar Ortiz, Javier},
title = {skforecast},
version = {0.13.0},
month = {8},
year = {2024},
license = {BSD-3-Clause},
url = {https://skforecast.org/},
doi = {10.5281/zenodo.8382788}
}
```

### Publications citing skforecast

<ul>

<li><p style="color:#808080; font-size:0.95em;">
Sanan, O., Sperling, J., Greene, D., & Greer, R. (2024, April). Forecasting Weather and Energy Demand for Optimization of Renewable Energy and Energy Storage Systems for Water Desalination. In 2024 IEEE Conference on Technologies for Sustainability (SusTech) (pp. 175-182). IEEE. <a href="https://doi.org/10.1109/SusTech60925.2024.10553570">https://doi.org/10.1109/SusTech60925.2024.10553570</a>
</p></li>

<li><p style="color:#808080; font-size:0.95em;">
Bojer, A. K., Biru, B. H., Al-Quraishi, A. M. F., Debelee, T. G., Negera, W. G., Woldesillasie, F. F., & Esubalew, S. Z. (2024). Machine learning and remote sensing based time series analysis for drought risk prediction in Borena Zone, Southwest Ethiopia. Journal of Arid Environments, 222, 105160. <a href="https://doi.org/10.1016/j.jaridenv.2024.105160">https://doi.org/10.1016/j.jaridenv.2024.105160</a>
</p></li>

<li><p style="color:#808080; font-size:0.95em;">
V. Negri, A. Mingotti, R. Tinarelli and L. Peretto, "Comparison Between the Machine Learning and the Statistical Approach to the Forecasting of Voltage, Current, and Frequency," 2023 IEEE 13th International Workshop on Applied Measurements for Power Systems (AMPS), Bern, Switzerland, 2023, pp. 01-06, doi: 10.1109/AMPS59207.2023.10297192. <a href="https://doi.org/10.1109/AMPS59207.2023.10297192">https://doi.org/10.1109/AMPS59207.2023.10297192</a>
</p></li>

<li><p style="color:#808080; font-size:0.95em;">
Marcillo Vera, F., Rosado, R., Zambrano, P., Velastegui, J., Morales, G., Lagla, L., & Herrera, A. (2024). Forecasting con Python, caso de estudio: visitas a las redes sociales en Ecuador con machine learning. CONECTIVIDAD, 5(2), 15-29.<a href=https://doi.org/10.37431/conectividad.v5i2.126 a>
</p></li>

<li><p style="color:#808080; font-size:0.95em;">OUKHOUYA, H., KADIRI, H., EL HIMDI, K., & GUERBAZ, R. (2023). Forecasting International Stock Market Trends: XGBoost, LSTM, LSTM-XGBoost, and Backtesting XGBoost Models. Statistics, Optimization & Information Computing, 12(1), 200-209. <a href="https://doi.org/10.19139/soic-2310-5070-1822">https://doi.org/10.19139/soic-2310-5070-1822</a></p>
</li>

<li><p style="color:#808080; font-size:0.95em;">DUDZIK, S., & Kowalczyk, B. (2023). Prognozowanie produkcji energii fotowoltaicznej z wykorzystaniem platformy NEXO i VRM Portal. Przeglad Elektrotechniczny, 2023(11). doi:10.15199/48.2023.11.41 </p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Polo J, Martín-Chivelet N, Alonso-Abella M, Sanz-Saiz C, Cuenca J, de la Cruz M. Exploring the PV Power Forecasting at Building Façades Using Gradient Boosting Methods. Energies. 2023; 16(3):1495. <a href="https://doi.org/10.3390/en16031495">https://doi.org/10.3390/en16031495</a></p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Popławski T, Dudzik S, Szeląg P. Forecasting of Energy Balance in Prosumer Micro-Installations Using Machine Learning Models. Energies. 2023; 16(18):6726. <a href="https://doi.org/10.3390/en16186726">https://doi.org/10.3390/en16186726</a></p>
</li>
<li><p style="color:#808080; font-size:0.95em;">Harrou F, Sun Y, Taghezouit B, Dairi A. Artificial Intelligence Techniques for Solar Irradiance and PV Modeling and Forecasting. Energies. 2023; 16(18):6731. <a href="https://doi.org/10.3390/en16186731">https://doi.org/10.3390/en16186731</a></p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Amara-Ouali, Y., Goude, Y., Doumèche, N., Veyret, P., Thomas, A., Hebenstreit, D., ... &amp; Phe-Neau, T. (2023). Forecasting Electric Vehicle Charging Station Occupancy: Smarter Mobility Data Challenge. arXiv preprint arXiv:2306.06142.</p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Emami, P., Sahu, A., &amp; Graf, P. (2023). BuildingsBench: A Large-Scale Dataset of 900K Buildings and Benchmark for Short-Term Load Forecasting. arXiv preprint arXiv:2307.00142.</p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Dang, HA., Dao, VD. (2023). Building Power Demand Forecasting Using Machine Learning: Application for an Office Building in Danang. In: Nguyen, D.C., Vu, N.P., Long, B.T., Puta, H., Sattler, KU. (eds) Advances in Engineering Research and Application. ICERA 2022. Lecture Notes in Networks and Systems, vol 602. Springer, Cham. <a href="https://doi.org/10.1007/978-3-031-22200-9_32">https://doi.org/10.1007/978-3-031-22200-9_32</a></p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Morate del Moral, Iván (2023). Predición de llamadas realizadas a un Call Center. Proyecto Fin de Carrera / Trabajo Fin de Grado, E.T.S.I. de Sistemas Informáticos (UPM), Madrid.</p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Lopez Vega, A., &amp; Villanueva Vargas, R. A. (2022). Sistema para la automatización de procesos hospitalarios de control para pacientes para COVID-19 usando machine learning para el Centro de Salud San Fernando.</p>
</li>

<li><p style="color:#808080; font-size:0.95em;">García Álvarez, J. D. (2022). Modelo predictivo de rentabilidad de criptomonedas para un futuro cercano.</p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Chilet Vera, Á. (2023). Elaboración de un algoritmo predictivo para la reposición de hipoclorito en los depósitos mediante técnicas de Machine Learning (Doctoral dissertation, Universitat Politècnica de València).</p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Bustinza Barrial, A. A., Bautista Abanto, A. M., Alva Alfaro, D. A., Villena Sotomayor, G. M., &amp; Trujillo Sabrera, J. M. (2022). Predicción de los valores de la demanda máxima de energía eléctrica empleando técnicas de machine learning para la empresa Nexa Resources–Cajamarquilla.</p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Morgado, K. Desarrollo de una técnica de gestión de activos para transformadores de distribución basada en sistema de monitoreo (Doctoral dissertation, Universidad Nacional de Colombia).</p>
</li>

<li><p style="color:#808080; font-size:0.95em;">Zafeiriou A., Chantzis G., Jonkaitis T., Fokaides P., Papadopoulos A., 2023, Smart Energy Strategy - A Comparative Study of Energy Consumption Forecasting Machine Learning Models, Chemical Engineering Transactions, 103, 691-696.</p>
</li>

</ul>


## Donating

If you found skforecast useful, you can support us with a donation. Your contribution will help to continue developing and improving this project. Many thanks! :hugging_face: :heart_eyes:

<a href="https://www.buymeacoffee.com/skforecast"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=skforecast&button_colour=f79939&font_colour=000000&font_family=Poppins&outline_colour=000000&coffee_colour=FFDD00" /></a>
<br>

[![paypal](https://www.paypalobjects.com/en_US/ES/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=D2JZSWRLTZDL6)


## License

[BSD-3-Clause License](https://github.com/JoaquinAmatRodrigo/skforecast/blob/master/LICENSE)