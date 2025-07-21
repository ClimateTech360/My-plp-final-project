def get_crisis_resources():
    """Return emergency and crisis mental health resources."""
    
    crisis_resources = {
        'immediate': [
            {
                'name': '988 Suicide & Crisis Lifeline',
                'phone': '988',
                'text': 'Text 988',
                'website': 'https://988lifeline.org',
                'description': '24/7 free and confidential support for people in distress and suicide prevention.'
            },
            {
                'name': 'Crisis Text Line',
                'phone': 'Text HOME to 741741',
                'text': '741741',
                'website': 'https://www.crisistextline.org',
                'description': '24/7 crisis support via text message.'
            },
            {
                'name': 'Emergency Services',
                'phone': '911',
                'website': 'https://www.911.gov',
                'description': 'For immediate medical or psychiatric emergencies.'
            },
            {
                'name': 'SAMHSA National Helpline',
                'phone': '1-800-662-4357',
                'website': 'https://www.samhsa.gov/find-help/national-helpline',
                'description': '24/7 treatment referral and information service for mental health and substance abuse.'
            },
            {
                'name': 'The Trevor Project (LGBTQ Youth)',
                'phone': '1-866-488-7386',
                'text': 'Text START to 678-678',
                'website': 'https://www.thetrevorproject.org',
                'description': '24/7 crisis support for LGBTQ youth.'
            },
            {
                'name': 'Trans Lifeline',
                'phone': '877-565-8860',
                'website': 'https://translifeline.org',
                'description': 'Crisis hotline staffed by transgender people for transgender people.'
            }
        ],
        
        'international': [
            {
                'name': 'Samaritans',
                'country': 'UK',
                'phone': '116 123',
                'website': 'https://www.samaritans.org'
            },
            {
                'name': 'Crisis Services Canada',
                'country': 'Canada',
                'phone': '1-833-456-4566',
                'website': 'https://www.crisisservicescanada.ca'
            },
            {
                'name': 'Lifeline Australia',
                'country': 'Australia',
                'phone': '13 11 14',
                'website': 'https://www.lifeline.org.au'
            },
            {
                'name': 'SOS Amitié',
                'country': 'France',
                'phone': '09 72 39 40 50',
                'website': 'https://www.sos-amitie.org'
            },
            {
                'name': 'Telefonseelsorge',
                'country': 'Germany',
                'phone': '0800 111 0 111',
                'website': 'https://www.telefonseelsorge.de'
            },
            {
                'name': 'Befrienders Worldwide',
                'country': 'Global',
                'phone': 'Various by country',
                'website': 'https://www.befrienders.org'
            }
        ],
        
        'specialized': [
            {
                'name': 'National Eating Disorders Association',
                'phone': '1-800-931-2237',
                'text': 'Text NEDA to 741741',
                'website': 'https://www.nationaleatingdisorders.org',
                'description': 'Support for eating disorders.'
            },
            {
                'name': 'RAINN National Sexual Assault Hotline',
                'phone': '1-800-656-4673',
                'website': 'https://www.rainn.org',
                'description': 'Support for sexual assault survivors.'
            },
            {
                'name': 'National Domestic Violence Hotline',
                'phone': '1-800-799-7233',
                'text': 'Text START to 88788',
                'website': 'https://www.thehotline.org',
                'description': 'Support for domestic violence situations.'
            },
            {
                'name': 'Veterans Crisis Line',
                'phone': '1-800-273-8255',
                'text': 'Text 838255',
                'website': 'https://www.veteranscrisisline.net',
                'description': '24/7 support for veterans and their families.'
            },
            {
                'name': 'NAMI Helpline',
                'phone': '1-800-950-6264',
                'website': 'https://www.nami.org',
                'description': 'Information and referrals for mental health resources.'
            }
        ]
    }
    
    return crisis_resources

def get_safety_planning_resources():
    """Return resources for safety planning and self-help."""
    
    safety_resources = {
        'safety_planning': [
            {
                'title': 'MY3 Safety Planning App',
                'description': 'Connects users to family, friends, and mental health professionals in times of crisis.',
                'website': 'https://my3app.org'
            },
            {
                'title': 'Safety Planning Guide',
                'description': 'Step-by-step guide to creating a personalized safety plan.',
                'website': 'https://suicidepreventionlifeline.org/create-safety-plan'
            }
        ],
        
        'immediate_coping': [
            {
                'title': 'Grounding Techniques',
                'description': '5-4-3-2-1 technique: Name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, 1 you can taste.',
                'website': 'https://www.healthline.com/health/grounding-techniques'
            },
            {
                'title': 'Box Breathing',
                'description': 'Breathe in for 4 counts, hold for 4, exhale for 4, hold for 4. Repeat.',
                'website': 'https://www.healthline.com/health/box-breathing'
            },
            {
                'title': 'Progressive Muscle Relaxation',
                'description': 'Systematically tense and relax different muscle groups.',
                'website': 'https://www.healthline.com/health/progressive-muscle-relaxation'
            }
        ]
    }
    
    return safety_resources
