def run(params):
    return {
        'project_name': 'Sample',
        'build_types': ['Debug', 'Release'],
        'archs': [
            {
                'arch': 'x86_64',
                'conan_arch': 'x86_64',
                'conan_profile': 'ezored_windows_app_profile',
            },
        ],
    }
