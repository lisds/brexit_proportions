test = {
  'name': 'Question simulated_prop_remain',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'simulated_prop_remain'
          >>> 'simulated_prop_remain' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'simulated_prop_remain'
          >>> # from its initial state (of ...)
          >>> simulated_prop_remain is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # res = rng.binomial(survey_n_total, uk_prop_remain, size=1000000) / survey_n_total
          # np.min(res), np.max(res)
          'code': r"""
          >>> 0.415 <= simulated_prop_remain <= 0.55
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
