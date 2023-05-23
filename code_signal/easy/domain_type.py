def domain_types(domains):
    """Write a function that labels the domains as "commercial",
       "organization", "network" or "information" for .com, .org, .net or
        .info respectively.
    >>> domains = ['how.to.do.it.info', 'business.com']
    >>> domain_types(domains)
    ['information', 'commercial']
    """

    return [ domain_type(domain) for domain in domains ]

def domain_type(domain):
    """Return the domain type of a URL.
    >>> domain_type(domain='example.com')
    'commercial'
    >>> domain_type(domain='beta.kernel.org')
    'organization'
    """
    domain_dict = {
        'com': "commercial",
        'org': "organization",
        'net': "network",
        'info': "information",
    }
    key = domain.split('.')[-1]

    return domain_dict[key]
