"""Install and build conan dependencies"""

import os

import ezored.app.const as const
from ezored.mod import file
from ezored.mod import log
from ezored.mod import runner
from ezored.mod import target


# -----------------------------------------------------------------------------
def run(params):
    proj_path = params['proj_path']
    target_name = params['target_name']
    target_config = target.get_target_config(proj_path, target_name)

    archs = target_config['archs']
    build_types = target_config['build_types']

    if archs and len(archs) > 0:
        for arch in archs:
            for build_type in build_types:
                log.info('Building for: {0}/{1}...'.format(
                    arch['conan_arch'],
                    build_type
                ))

                # conan install
                build_dir = os.path.join(
                    proj_path,
                    const.DIR_NAME_BUILD,
                    target_name,
                    build_type,
                    arch['conan_arch'],
                    const.DIR_NAME_BUILD_CONAN,
                )

                file.remove_dir(build_dir)
                file.create_dir(build_dir)

                run_args = [
                    'conan',
                    'install',
                    os.path.join(
                        proj_path,
                        const.DIR_NAME_FILES,
                        const.DIR_NAME_FILES_TARGETS,
                        target_name,
                        const.DIR_NAME_FILES_TARGET_CONAN,
                        const.DIR_NAME_FILES_TARGET_CONAN_RECIPE,
                        const.FILE_NAME_FILES_TARGET_CONAN_RECIPE_CONANFILE_PY,
                    ),
                    '--profile',
                    arch['conan_profile'],
                    '-s',
                    'arch={0}'.format(arch['conan_arch']),
                    '-s',
                    'build_type={0}'.format(build_type),
                    '-o',
                    '{0}:ios_arch={1}'.format(
                        target_name,
                        arch['arch']
                    ),
                    '-o',
                    '{0}:ios_platform={1}'.format(
                        target_name,
                        arch['platform']
                    ),
                    '-o',
                    '{0}:ios_deployment_target={1}'.format(
                        target_name,
                        target_config['min_version']
                    ),
                    '-o',
                    '{0}:enable_bitcode={1}'.format(
                        target_name,
                        ('1' if target_config['bitcode'] else '0')
                    ),
                    '-o',
                    '{0}:enable_arc={1}'.format(
                        target_name,
                        ('1' if target_config['enable_arc'] else '0')
                    ),
                    '-o',
                    '{0}:enable_visibility={1}'.format(
                        target_name,
                        ('1' if target_config['enable_visibility'] else '0')
                    ),
                    '-o',
                    '{0}:cmake_toolchain_file={1}'.format(
                        target_name,
                        os.path.join(
                            proj_path,
                            const.DIR_NAME_FILES,
                            const.DIR_NAME_FILES_CMAKE,
                            const.DIR_NAME_FILES_CMAKE_TOOLCHAINS,
                            'ios.cmake',
                        )
                    ),
                    '-o',
                    'darwin-toolchain:bitcode={0}'.format(
                        'True' if target_config['bitcode'] else 'False'
                    ),
                    '--build=missing',
                    '--update',
                ]

                runner.run(
                    run_args,
                    build_dir
                )
    else:
        log.error('Arch list for "{0}" is invalid or empty'.format(
            target_name
        ))
