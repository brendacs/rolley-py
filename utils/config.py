PREFIX = ">"
HOST_CHANNEL = "bot-development"

# INACCESSIBLE_ROLES = [role_name, role_name, ...]

INACCESSIBLE_ROLES = {"the imagineers", "Admin", "mods", "Interviewers",
                      "Recruiter", "Hiring Manager", "Bot Creation", "Website Mod"}

# ROLES = { role_group: { emoji : role_label, ... }, ... }

ROLES = {
    'clears': {
        '❌'        :'0', 
        '🙅'        :'1',
        'stopblob' :'2'
    },
    'languages': {
        'c_plus'   :'C++',
        'c_reg'    :'C',
        'c_sharp'  :'C#',
        'go'       :'Go',
        'haskell'  :'Haskell',
        'java'     :'Java',
        'js'       :'Javascript',
        '👄'        :'Lisp',
        'lua'      :'Lua',
        'obj_c'    :'Objective-C',
        'php'      :'PHP',
        'python'   :'Python',
        '🇷'        :'R',
        'ruby'     :'Ruby',
        'rust'     :'Rust',
        'scala'    :'Scala',
        'sql'      :'SQL',
        'swift'    :'Swift'
    },
    'seniorities': {
        '🎓' : 'Student',  
        '🤓' : 'Intern',
        '💼' : 'Junior Developer', 
        '👔' : 'Mid-level Developer',
        '👴' : 'Senior Developer'
    },
    'xtra': {
        '💡'  : 'Notifications',
        '🔔'  : 'Interview Notifications',
        'vet': 'Military Veteran'
    }
}

# EMBEDS = [(title, description), (title, description), ...]

EMBEDS = [
    ("React for Roles with Rolley!",
     ("Add a reaction on the below messages to add a role, remove a reaction to remove the role. "
      "If you already have the role, clicking a reaction will not do anything. "
      "However, if you have the role and react then unreact, your role will be removed. "
      "Click any react on this message to clear all of your self-assignable roles. "
      "If it is unclear what emojis are which, hover over the emoji to see its name.")),
    ("Language Roles", "Add a programming language role, but don\'t abuse them! Possible roles: {}."
        .format(', '.join(sorted(ROLES['languages'].keys())))),
    ("Seniority Roles",
     "You are only allowed one seniority role that best reflects where you\'re at in your career. Possible roles: {}. "
     "Emoji key: Student = mortar_board, Intern = nerd, Junior Developer = briefcase, "
     "Mid-level Developer = necktie, Senior Developer = older_man."
        .format(', '.join(sorted(ROLES['seniorities'].keys())))),
    ("Miscellaneous", "These are utility roles, mostly. Notifications: opt-in to global notifications, "
     "Interview Notifications: opt-in to interview notifications, "
     "Military Veteran: choose this role if you are a military veteran.")
]
