PREFIX = '>'
CHANNEL = '#roles'

# ROLES = { role_group: { role_name: emote_name, ... }, ... }

ROLES = {
    'clears': {
        '0': '❌',
        '1': '🙅',
        '2': 'stopblob'
    },
    'languages': {
        'C++': 'cplus',
        'C': 'creg',
        'C#': 'csharp',
        'Go': 'go',
        'Haskell': 'haskell',
        'Javascript': 'js',
        'Lisp': '👄',
        'Lua': 'lua',
        'Objective-C': '🍎',
        'PHP': 'php',
        'Python': 'python',
        'R': '🇷',
        'Ruby': 'ruby',
        'Rust': 'rust',
        'Scala': 'scala',
        'SQL': 'sql',
        'Swift': 'swift'
    },
    'seniorities': {
        'Student': '🎓',
        'Intern': '🤓',
        'Junior Developer': '💼',
        'Mid-level Developer': '👔',
        'Senior Developer': '👴'
    },
    'xtra': {
        'Notifications': '💡',
        'Interview Notifications': '🔔',
        'Military Veteran': 'vet'
    }
}

# EMBEDS = [(title, description), (title, description), ...]

EMBEDS = [
    ("React for Roles with Rolley!",
     ("Add a reaction on the below messages to add a role, remove a reaction to remove the role. "
      "If you already have the role, clicking a reaction will not do anything. "
      "However, if you have the role and react then unreact, your role will be removed. "
      "Click any react on this message to clear all of your self-assignable roles.")),
    ("Language Roles", "Add a programming language role, but don\'t abuse them! Possible roles: {}"
        .format(', '.join(sorted(ROLES['languages'].keys())))),
    ("Seniority Roles",
     "You are only allowed one seniority role that best reflects where you\'re at in your career. Possible roles: {}"
        .format(', '.join(sorted(ROLES['seniorities'].keys())))),
    ("Miscellaneous", "These are utility roles, mostly. Notifications: opt-in to global notifications, "
     "Interview Notifications: opt-in to interview notifications, "
     "Military Veteran: choose this role if you are a military veteran")
]
