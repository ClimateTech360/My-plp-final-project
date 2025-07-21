def get_kenya_mental_health_resources():
    """Return Kenya-specific mental health resources and information."""
    
    resources = {
        'professional': [
            {
                'title': 'Kenya Association of Professional Counsellors (KAPC)',
                'description': 'Find licensed counsellors and therapists across Kenya. Established in 1990, provides professional counseling training and services.',
                'website': 'https://www.kapc.or.ke',
                'phone': '+254 20 3741051',
                'helpline': '0800 724 263 (Toll-Free)',
                'email': 'nairobi@kapc.or.ke'
            },
            {
                'title': 'Mathari National Teaching and Referral Hospital',
                'description': 'Kenya\'s largest psychiatric hospital with over 500 beds, providing specialized mental health services, training and research.',
                'website': 'https://mntrh.go.ke',
                'phone': '+254 20 2337694',
                'email': 'info@mntrh.go.ke'
            },
            {
                'title': 'Kenya Red Cross - Psychosocial Support',
                'description': 'Emergency psychosocial support services and community mental health programs nationwide.',
                'website': 'https://www.redcross.or.ke',
                'phone': '+254 20 3950000',
                'emergency': '1199 (Toll-Free on Safaricom)',
                'email': 'info@redcross.or.ke'
            },
            {
                'title': 'Kenyatta National Hospital - Mental Health',
                'description': 'National referral hospital with comprehensive psychiatric services and youth mental health center.',
                'website': 'https://knh.or.ke',
                'phone': '+254 20 2726300',
                'youth_center': 'Free services every Tuesday 8am-4pm (ages 25 and under)'
            },
            {
                'title': 'Moi Teaching and Referral Hospital - Eldoret',
                'description': 'Regional referral hospital with psychiatric services covering Western Kenya region.',
                'website': 'https://mtrh.go.ke',
                'phone': '+254 53 2063300'
            }
        ],
        
        'educational': [
            {
                'title': 'Ministry of Health - Mental Health Division',
                'description': 'Official government resource for mental health policies, programs, and the Kenya Mental Health Action Plan 2021-2025.',
                'website': 'https://mental.health.go.ke'
            },
            {
                'title': 'Kenya Association of Professional Counsellors (KAPC)',
                'description': 'Professional training institution offering certificate to diploma level counseling courses and resources.',
                'website': 'https://www.kapc.or.ke'
            },
            {
                'title': 'What\'s Eating My Mind',
                'description': 'Mental health awareness platform providing educational content and emergency resources for Kenya.',
                'website': 'https://www.whatseatingmymind.com'
            },
            {
                'title': 'Speak Up Kenya',
                'description': 'Mental health advocacy organization providing educational resources and crisis support information.',
                'website': 'https://speakup.co.ke'
            },
            {
                'title': 'Mathari National Teaching and Referral Hospital',
                'description': 'Kenya\'s premier psychiatric hospital providing training, research, and educational resources.',
                'website': 'https://mntrh.go.ke'
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
                'name': 'Kenya Red Cross Emergency',
                'phone': '1199 (Toll-Free on Safaricom)',
                'alternative': '+254 703 037 000',
                'website': 'https://www.redcross.or.ke',
                'description': '24/7 emergency services including mental health crisis support.'
            },
            {
                'name': 'Befrienders Kenya Crisis Line',
                'phone': '+254 722 178 177',
                'alternative': '+254 736 542 304',
                'website': 'https://befrienders.org/find-support-now/befrienders-kenya/',
                'email': 'befrienderskenya@gmail.com',
                'description': 'Free confidential emotional support and suicide prevention. Monday-Friday 9am-5pm.',
                'address': 'La Colline Gardens, Masaba Road, Upper Hill, Nairobi'
            },
            {
                'name': 'EMKF Suicide Prevention Hotline',
                'phone': '0800 723 253',
                'website': 'https://speakup.co.ke',
                'description': 'Free nationwide suicide prevention hotline operated by trained counselors.'
            },
            {
                'name': 'Niskize Crisis Center',
                'phone': '0900 620 800',
                'alternative': '+254 718 227 440',
                'website': 'https://www.whatseatingmymind.com',
                'description': '24-hour crisis intervention and suicide prevention services.'
            },
            {
                'name': 'Mental 360 Youth Line',
                'phone': '+254 776 543 099',
                'website': 'https://mental360.co.ke',
                'description': '24/7 mental health support specifically for people aged 25 and under.'
            },
            {
                'name': 'CBT Kenya Crisis Support',
                'phone': '+254 739 935 333',
                'alternative': '+254 756 454 585',
                'website': 'https://cbtkenya.org',
                'description': 'Crisis counseling and cognitive behavioral therapy support.'
            }
        ],
        
        'regional': [
            {
                'name': 'KAPC Nairobi Branch',
                'region': 'Nairobi County',
                'phone': '+254 20 3741051',
                'mobile': '+254 721 296912',
                'address': '2nd Floor, Kalson Towers, The Crescent, Off Parklands Road'
            },
            {
                'name': 'KAPC Mombasa Branch',
                'region': 'Coast Region',
                'phone': '+254 41 2493050',
                'mobile': '+254 725 797888',
                'address': 'Kenyatta Avenue, Narok Rd, Mombasa Real Estate Building'
            },
            {
                'name': 'KAPC Kisumu Branch',
                'region': 'Western Kenya',
                'phone': '+254 57 2027071',
                'mobile': '+254 733 868610',
                'address': 'Mamboleo Junction, off Kakamega Road'
            },
            {
                'name': 'KAPC Eldoret Branch',
                'region': 'Rift Valley',
                'phone': '+254 53 2030682',
                'mobile': '+254 712 141272',
                'address': 'Rehema Complex, Ronald Ngala Street'
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