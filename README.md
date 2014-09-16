# Frasco-Countries

Makes information from [pycountry](https://pypi.python.org/pypi/pycountry) available as actions. Provides
form fields for countries, languages and currencies. Will use information
from [Frasco-Geoip](https://github.com/frascoweb/frasco-geopip) if available to select the default entry.

## Installation

    pip install frasco-countries

## Setup

Feature name: countries

Options:

 - *use_geolocation_as_default*: whether to use geolocation information when available
   to set the default country (default: True)

## Global variables

 - `$current_country`: will be automatically set on every requests once `set_current_country()` has
   been called or if geolocation is available via Frasco-Geoip.

## Actions

### set\_current\_country

Sets the current country for the current session (ie. will be persisted through requests).

Options:

 - *alpha2*: the country's alpha2 code (optional, must be present if *country* is not)
 - *country*: a pycountry country object (optional, must be present if *alpha2* is not)
 - *is_global*: whether this affects only the current context or will be persisted using the session (default: True)

### get\_country

Calls `pycountry.countries.get()`.

Options (one of):

  - *alpha2* (default): the country's alpha2 code
  - *slug*: the country name as a slug
  - any other `countries.get()` arguments

Returns a country object.  
Default variable assignment: `$country`

### geolocate\_country

Calls `pycountry.countries.get()` using the geolocation information provided by Frasco-Geoip.

Returns a country object.  
Default variable assignment: `$country`

### get\_currency

Calls `pycountry.currencies.get()`.

Options (one of):

  - *letter* (default): the currency's letter
  - any other `currencies.get()` arguments

Returns a currency object.  
Default variable assignment: `$currency`

### get\_language

Calls `pycountry.languages.get()`.

Options (one of):

  - *alpha2* (default): the language's alpha2 code
  - any other `languages.get()` arguments

Returns a language object.  
Default variable assignment: `$language`

## Template globals

### `list_countries()`

Returns a list of country objects of all available countries

### `country_name($alpha2)`

Returns the name of the country with the given alpha2 code

### `country_currency($country_alpha2_or_obj)`

Returns the currency code for the country reference by its alpha2 code or by a country object.

## Form fields

Three WTForms form fields are provided, all of them being subclasses of `SelectField`:

 - `frasco_countries.form.CountryField`
 - `frasco_countries.form.LanguageField`
 - `frasco_countries.form.CurrencyField`

Their default value will be taken from the current country.

If Frasco-Forms is used, these fields will be available under the names:

 - *country*
 - *language*
 - *currency*

