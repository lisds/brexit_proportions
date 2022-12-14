test = {
  'name': 'Question simulated_props',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'simulated_props'
          >>> 'simulated_props' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'simulated_props'
          >>> # from its initial state (of ...)
          >>> simulated_props is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(simulated_props)
          10000
          """,
          'hidden': False,
          'locked': False
        },
        {
          # res = rng.binomial(survey_n_total, uk_prop_remain, size=1000000) / survey_n_total
          # np.min(res), np.max(res)
          'code': r"""
          >>> 0.48 <= np.mean(simulated_props) <= 0.482
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # res = rng.binomial(survey_n_total, uk_prop_remain, size=(10000, 10000)) / survey_n_total
          # means = np.mean(res, axis=1)
          # stds = np.std(res, axis=1)
          # np.min(means), np.max(means)
          # np.min(stds), np.max(stds)
          'code': r"""
          >>> 0.0134 <= np.std(simulated_props) <= 0.0142
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
