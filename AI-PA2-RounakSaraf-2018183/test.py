from durable.lang import *

with ruleset('interests'):
    # will be triggered by 'interests' facts
    @when_all((m.area == 'human-like-conversations') & (m.type == 'notheory') )
    def hci(c):
        c.assert_fact('skills', { 'field': 'probability' })
        c.assert_fact({ 'subject': 'choose', 'predicate': 'elective', 'object': 'natural language processing' })
        
    @when_all((m.area == 'human-like-conversations') & (m.type == 'theory') )
    def hci(c):
        c.assert_fact('skills', { 'field': 'probability' })
        c.assert_fact({ 'subject': 'choose', 'predicate': 'elective', 'object': 'natural language processing' })
        c.assert_fact('preferences', { 'type': 'nltheory' })

    @when_all((m.area == 'human-like-interactions') & (m.type == 'theory') )
    def rob(c):
        c.assert_fact('skills', { 'field': 'ai-ml' })
        c.assert_fact({ 'subject': 'choose', 'predicate': 'elective', 'object': 'robotics' })
        c.assert_fact('preferences', { 'type': 'mltheory' })

    @when_all((m.area == 'human-like-interactions') & (m.type == 'notheory') )
    def rob(c):
        c.assert_fact('skills', { 'field': 'ai-ml' })
        c.assert_fact({ 'subject': 'choose', 'predicate': 'elective', 'object': 'robotics' })

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))

with ruleset('skills'):
    @when_all((m.field == 'probability'))
    def mathc(d):
        d.assert_fact({ 'subject': 'take Probability and Statistics course' })

    @when_all((m.field == 'ai-ml'))
    def mathc(d):
        d.assert_fact({ 'subject': 'take AI course' })
        d.assert_fact({ 'subject': 'take ML course' })
        d.assert_fact( {'subject': 'take DL course' })

    @when_all(+m.subject)
    def output(d):
        print('Fact: {0}'.format(d.m.subject))

with ruleset('preferences'):
    @when_all((m.type == 'mltheory'))
    def mathct(e):
        e.assert_fact({ 'subject': 'take DL theory course'})

    @when_all((m.type == 'nltheory'))
    def mathct(e):
        e.assert_fact({ 'subject': 'take NLP foundations course'})


    @when_all(+m.subject)
    def output(c):
        print('Fact: {0}'.format(c.m.subject))


assert_fact('interests', { 'area': 'human-like-interactions', 'type': 'theory' })
