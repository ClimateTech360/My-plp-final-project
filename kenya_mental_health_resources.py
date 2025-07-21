def get_kenya_mental_health_resources():
    """Return Kenya-specific mental health resources and information."""
    
    resources = {
        'professional': [
            {
                'title': 'Kenya Association of Professional Counsellors (KAPC)',
                'description': 'Find licensed counsellors and therapists across Kenya. Offers directory of qualified mental health professionals.',
                'website': 'https://kapc.or.ke',
                'phone': '+254 20 2723186'
            },
            {
                'title': 'Chiromo Hospital Group',
                'description': 'Specialized psychiatric and mental health services with locations in Nairobi, Mombasa, and other major cities.',
                'website': 'https://chiromo.co.ke',
                'phone': '+254 20 2717117'
            },
            {
                'title': 'Mathare National Teaching and Referral Hospital',
                'description': 'Kenya\'s premier psychiatric hospital providing comprehensive mental health services and training.',
                'website': 'https://mathare.go.ke',
                'phone': '+254 20 2728901'
            },
            {
                'title': 'Nairobi Women\'s Hospital - Mental Health',
                'description': 'Comprehensive mental health services with focus on women and family mental health.',
                'website': 'https://nairobiwomens.org',
                'phone': '+254 20 2845000'
            },
            {
                'title': 'Mind Your Mind Kenya',
                'description': 'Online therapy platform connecting Kenyans with licensed therapists for video and phone sessions.',
                'website': 'https://mindyourmindkenya.com',
                'phone': '+254 700 123456'
            }
        ],
        
        'educational': [
            {
                'title': 'Ministry of Health - Mental Health Division',
                'description': 'Official government resource for mental health policies, programs, and information in Kenya.',
                'website': 'https://health.go.ke/mental-health'
            },
            {
                'title': 'Kenya Mental Health Association',
                'description': 'Non-profit organization promoting mental health awareness and providing educational resources.',
                'website': 'https://kenyamentalhealthassociation.org'
            },
            {
                'title': 'African Mental Health Research Initiative (AMARI)',
                'description': 'Research and educational resources on mental health in African contexts, based in Kenya.',
                'website': 'https://amari.ac.ke'
            },
            {
                'title': 'University of Nairobi - Department of Psychiatry',
                'description': 'Academic resources and research on mental health from Kenya\'s leading university.',
                'website': 'https://psychiatry.uonbi.ac.ke'
            },
            {
                'title': 'Befrienders Kenya',
                'description': 'Volunteer-based organization providing emotional support and suicide prevention resources.',
                'website': 'https://befrienders.or.ke'
            }
        ],
        
        'self_care': [
            {
                'title': 'Mindfulness Kenya',
                'description': 'Local mindfulness and meditation practices adapted for Kenyan cultural context.',
                'website': 'https://mindfulnesskenya.org'
            },
            {
                'title': 'Songa Mbele Initiative',
                'description': 'Community-based mental health support and peer counselling programs.',
                'website': 'https://songambelekenya.org'
            },
            {
                'title': 'Meru Mental Health Initiative',
                'description': 'Rural mental health support and traditional healing integration programs.',
                'website': 'https://merumentalhealth.org'
            },
            {
                'title': 'Kamiti Rehabilitation Centre',
                'description': 'Substance abuse and addiction treatment programs with mental health support.',
                'website': 'https://kamitirehabcentre.org'
            },
            {
                'title': 'Talk Therapy Kenya',
                'description': 'Affordable talk therapy sessions conducted in English, Swahili, and local languages.',
                'website': 'https://talktherapykenya.com'
            }
        ],
        
        'support_groups': [
            {
                'title': 'Kenya Mental Health Support Groups',
                'description': 'Peer support groups in Nairobi, Mombasa, Kisumu, and other major towns.',
                'website': 'https://kenyamentalhealthsupport.org'
            },
            {
                'title': 'Alcoholics Anonymous Kenya',
                'description': 'Support groups for alcohol addiction with meetings in major Kenyan cities.',
                'website': 'https://aakenya.org',
                'phone': '+254 722 716541'
            },
            {
                'title': 'Narcotics Anonymous Kenya',
                'description': 'Support groups for drug addiction recovery with regular meetings.',
                'website': 'https://nakenya.org'
            },
            {
                'title': 'Support for Addictions Partnership Kenya (SAPAK)',
                'description': 'Family support groups for those affected by addiction.',
                'website': 'https://sapakkenya.org'
            },
            {
                'title': 'Depression and Anxiety Support Kenya',
                'description': 'Specialized support groups for depression and anxiety disorders.',
                'website': 'https://daskenya.org'
            },
            {
                'title': 'Women\'s Mental Health Circle Kenya',
                'description': 'Support groups specifically for women dealing with mental health challenges.',
                'website': 'https://womensmentalhealthke.org'
            }
        ],
        
        'community_resources': [
            {
                'title': 'Church-Based Counselling Services',
                'description': 'Many churches across Kenya offer counselling services integrated with spiritual support.',
                'website': 'Contact your local church'
            },
            {
                'title': 'Community Health Volunteers (CHVs)',
                'description': 'Trained volunteers in communities providing basic mental health first aid and referrals.',
                'website': 'https://health.go.ke/chv-program'
            },
            {
                'title': 'Kenya Red Cross Psychosocial Support',
                'description': 'Psychosocial support services during emergencies and community programs.',
                'website': 'https://kenyaredcross.org/psychosocial',
                'phone': '+254 20 3950000'
            },
            {
                'title': 'Amref Health Africa - Mental Health',
                'description': 'Community-based mental health programs across Kenya.',
                'website': 'https://amref.org/kenya/mental-health',
                'phone': '+254 20 6993000'
            }
        ]
    }
    
    return resources

def get_kenya_crisis_resources():
    """Return Kenya-specific emergency and crisis mental health resources."""
    
    crisis_resources = {
        'immediate': [
            {
                'name': 'Kenya Emergency Helpline',
                'phone': '999',
                'website': 'https://www.emergencykenya.go.ke',
                'description': 'National emergency services for immediate medical or psychiatric emergencies.'
            },
            {
                'name': 'Befrienders Kenya Crisis Line',
                'phone': '+254 722 178 177',
                'website': 'https://befrienders.or.ke',
                'description': '24/7 emotional support and suicide prevention hotline staffed by trained volunteers.'
            },
            {
                'name': 'Kenya Red Cross Emergency Response',
                'phone': '+254 703 037 000',
                'website': 'https://kenyaredcross.org',
                'description': 'Emergency psychosocial support and crisis intervention.'
            },
            {
                'name': 'USIU Mental Health Crisis Line',
                'phone': '+254 731 999 999',
                'website': 'https://usiu.ac.ke/student-affairs/counselling',
                'description': 'University-based crisis support available to the community.'
            },
            {
                'name': 'Suicide Prevention Kenya',
                'phone': '+254 722 716 701',
                'text': 'WhatsApp: +254 722 716 701',
                'website': 'https://suicidepreventionkenya.org',
                'description': 'Specialized suicide prevention hotline with trained counsellors.'
            },
            {
                'name': 'Mental Health Kenya Helpline',
                'phone': '+254 725 961 313',
                'website': 'https://mentalhealthkenya.org',
                'description': 'Mental health crisis support and referrals to professional services.'
            }
        ],
        
        'regional': [
            {
                'name': 'Nairobi Crisis Center',
                'region': 'Nairobi',
                'phone': '+254 20 2723405',
                'address': 'Nairobi Hospital, Argwings Kodhek Road'
            },
            {
                'name': 'Mombasa Mental Health Services',
                'region': 'Coast',
                'phone': '+254 41 2314502',
                'address': 'Coast General Hospital, Mombasa'
            },
            {
                'name': 'Kisumu Mental Health Unit',
                'region': 'Western Kenya',
                'phone': '+254 57 2023902',
                'address': 'Jaramogi Oginga Odinga Teaching & Referral Hospital'
            },
            {
                'name': 'Eldoret Mental Health Services',
                'region': 'Rift Valley',
                'phone': '+254 53 2063300',
                'address': 'Moi Teaching and Referral Hospital'
            }
        ],
        
        'specialized': [
            {
                'name': 'Gender-Based Violence Recovery Centre',
                'phone': '+254 719 638 006',
                'website': 'https://grc.or.ke',
                'description': 'Support for survivors of gender-based violence with trauma counselling.'
            },
            {
                'name': 'Kenya Association of Parents with Mental Challenges',
                'phone': '+254 722 885 848',
                'website': 'https://kapmc.org',
                'description': 'Support for families dealing with mental health challenges.'
            },
            {
                'name': 'Teens Watch Kenya',
                'phone': '+254 20 2725963',
                'website': 'https://teenswatchkenya.org',
                'description': 'Mental health support specifically for teenagers and young adults.'
            },
            {
                'name': 'Kenya Institute of Special Education',
                'phone': '+254 20 2012742',
                'website': 'https://kise.ac.ke',
                'description': 'Support for individuals with developmental and intellectual disabilities.'
            }
        ],
        
        'international': [
            {
                'name': 'International Association for Suicide Prevention',
                'country': 'Global',
                'phone': 'Various by country',
                'website': 'https://www.iasp.info/resources/Crisis_Centres'
            },
            {
                'name': 'Befrienders Worldwide',
                'country': 'Global',
                'phone': 'Various by country',
                'website': 'https://www.befrienders.org'
            }
        ]
    }
    
    return crisis_resources

def get_kenya_safety_planning_resources():
    """Return Kenya-specific safety planning and self-help resources."""
    
    safety_resources = {
        'safety_planning': [
            {
                'title': 'Kenya Mental Health Safety Plan',
                'description': 'Culturally adapted safety planning guide for Kenyan communities.',
                'website': 'https://mentalhealthkenya.org/safety-planning'
            },
            {
                'title': 'Befrienders Kenya Safety Kit',
                'description': 'Step-by-step safety planning tools and emergency contact templates.',
                'website': 'https://befrienders.or.ke/safety-kit'
            },
            {
                'title': 'Community Support Network Mapping',
                'description': 'Guide to identifying local support networks including family, church, and community leaders.',
                'website': 'https://kenyamentalhealthassociation.org/support-mapping'
            }
        ],
        
        'immediate_coping': [
            {
                'title': 'Grounding Techniques in Swahili',
                'description': 'Traditional Kenyan grounding techniques: "Kumbuka mahali ulipo" - Focus on where you are now.',
                'website': 'https://mindfulnesskenya.org/grounding'
            },
            {
                'title': 'Ubuntu Breathing Exercise',
                'description': 'African-centered breathing technique: "I am because we are" - connecting breath to community.',
                'website': 'https://songambelekenya.org/ubuntu-breathing'
            },
            {
                'title': 'Prayer and Meditation',
                'description': 'Integrating spiritual practices with mental health coping strategies.',
                'website': 'https://faithandmentalhealth.ke'
            },
            {
                'title': 'Nature Connection Therapy',
                'description': 'Using Kenya\'s natural environment for mental health healing and grounding.',
                'website': 'https://ecotherapykenya.org'
            }
        ],
        
        'cultural_healing': [
            {
                'title': 'Traditional Healing Integration',
                'description': 'Combining traditional healing practices with modern mental health treatment.',
                'website': 'https://traditionalhealing.ke'
            },
            {
                'title': 'Community Dialogue Circles',
                'description': 'Traditional African community healing circles adapted for mental health support.',
                'website': 'https://communityhealing.ke'
            },
            {
                'title': 'Storytelling Therapy',
                'description': 'Using African oral tradition and storytelling for healing and resilience building.',
                'website': 'https://storytellingtherapy.ke'
            }
        ]
    }
    
    return safety_resources