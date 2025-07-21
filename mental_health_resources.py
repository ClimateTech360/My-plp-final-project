def get_mental_health_resources():
    """Return comprehensive mental health resources and information."""
    
    resources = {
        'professional': [
            {
                'title': 'Psychology Today',
                'description': 'Find licensed therapists, psychiatrists, and mental health professionals in your area. Includes detailed profiles, specialties, and insurance information.',
                'website': 'https://www.psychologytoday.com/us/therapists'
            },
            {
                'title': 'BetterHelp',
                'description': 'Online therapy platform connecting you with licensed therapists for video, phone, and messaging sessions.',
                'website': 'https://www.betterhelp.com'
            },
            {
                'title': 'Talkspace',
                'description': 'Online therapy services with text, audio, and video messaging with licensed therapists.',
                'website': 'https://www.talkspace.com'
            },
            {
                'title': 'SAMHSA Treatment Locator',
                'description': 'Government resource to find mental health and substance abuse treatment facilities in your area.',
                'website': 'https://findtreatment.samhsa.gov/',
                'phone': '1-800-662-4357'
            },
            {
                'title': 'Crisis Text Line',
                'description': '24/7 crisis support via text message. Trained crisis counselors provide support for any crisis.',
                'website': 'https://www.crisistextline.org',
                'phone': 'Text HOME to 741741'
            }
        ],
        
        'educational': [
            {
                'title': 'National Institute of Mental Health (NIMH)',
                'description': 'Comprehensive information about mental health conditions, treatments, and research.',
                'website': 'https://www.nimh.nih.gov'
            },
            {
                'title': 'Mental Health America',
                'description': 'Educational resources, screening tools, and advocacy for mental health awareness.',
                'website': 'https://www.mhanational.org'
            },
            {
                'title': 'Anxiety and Depression Association of America',
                'description': 'Information about anxiety and depression disorders, treatment options, and support resources.',
                'website': 'https://adaa.org'
            },
            {
                'title': 'National Alliance on Mental Illness (NAMI)',
                'description': 'Education, support groups, and advocacy for individuals and families affected by mental illness.',
                'website': 'https://www.nami.org'
            },
            {
                'title': 'Depression and Bipolar Support Alliance',
                'description': 'Peer support and educational resources for mood disorders.',
                'website': 'https://www.dbsalliance.org'
            }
        ],
        
        'self_care': [
            {
                'title': 'Mindfulness Meditation',
                'description': 'Free guided meditations and mindfulness exercises to reduce stress and improve mental well-being.',
                'website': 'https://www.mindful.org/meditation/mindfulness-getting-started'
            },
            {
                'title': 'Headspace',
                'description': 'Meditation and mindfulness app with guided sessions for stress, anxiety, and sleep.',
                'website': 'https://www.headspace.com'
            },
            {
                'title': 'Calm',
                'description': 'Meditation, sleep stories, and relaxation techniques for mental wellness.',
                'website': 'https://www.calm.com'
            },
            {
                'title': 'Mood Meter',
                'description': 'Emotional intelligence app to help identify, understand, and regulate emotions.',
                'website': 'https://www.moodmeterapp.com'
            },
            {
                'title': 'DBT Self-Help',
                'description': 'Dialectical Behavior Therapy skills and techniques for emotional regulation.',
                'website': 'https://www.dbtselfhelp.com'
            },
            {
                'title': 'Grounding Techniques',
                'description': 'Learn 5-4-3-2-1 and other grounding techniques to manage anxiety and panic.',
                'website': 'https://www.healthline.com/health/grounding-techniques'
            }
        ],
        
        'support_groups': [
            {
                'title': 'NAMI Support Groups',
                'description': 'Peer support groups for individuals with mental health conditions and their families.',
                'website': 'https://www.nami.org/Support-Education/Support-Groups'
            },
            {
                'title': 'Mental Health Support Groups',
                'description': 'Online and in-person support groups for various mental health conditions.',
                'website': 'https://www.mentalhealthsupportgroups.com'
            },
            {
                'title': '7 Cups',
                'description': 'Free online emotional support and counseling through trained listeners.',
                'website': 'https://www.7cups.com'
            },
            {
                'title': 'Depression and Bipolar Support Alliance Groups',
                'description': 'Peer-led support groups for mood disorders.',
                'website': 'https://www.dbsalliance.org/support/chapters-and-support-groups'
            },
            {
                'title': 'Anxiety Support Groups',
                'description': 'Support groups specifically for anxiety disorders and panic attacks.',
                'website': 'https://adaa.org/supportgroups'
            },
            {
                'title': 'Suicide Loss Support Groups',
                'description': 'Support for those who have lost someone to suicide.',
                'website': 'https://suicidology.org/resources/suicide-loss-support-groups'
            }
        ]
    }
    
    return resources
