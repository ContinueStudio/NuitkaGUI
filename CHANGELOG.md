# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.13.24](https://github.com/271374667/NuitkaGUI/compare/v0.2.6...v0.13.24) - 2024-11-01

- ⬆️ 升级(version.py)：将版本号从0.2.6更新为0.13.24 [`bd18072`](https://github.com/271374667/NuitkaGUI/commit/bd180721aa685e44d96e4da766a67b70b20ebf3d)
- ♻️ refactor(command.py, command_manager.py, args_view.py)：优化命令解析和处理逻辑 [`aaf9097`](https://github.com/271374667/NuitkaGUI/commit/aaf90972460b51bf33d735d2d988ed6c82515569)
- ✨ feat(command.py, command_manager.py, manager_plugin.py, plugin_presenter.py)：增强插件管理功能，添加信号总线支持 [`7526013`](https://github.com/271374667/NuitkaGUI/commit/7526013f6668e6e0be0ddc60ab0e717e9125d402)
- ♻️ refactor(command.py)：移除不必要的widget更新调用 [`490ed1f`](https://github.com/271374667/NuitkaGUI/commit/490ed1f4c56617314d2524dde8906cc2d3e8748d)
- ✨ feat(command.py, command_manager.py, args_view.py)：为命令类添加解析功能 [`13cb1a2`](https://github.com/271374667/NuitkaGUI/commit/13cb1a249eaf8b1b37b3239bb556927a6c01d050)
- ✨ feat(config.py, setting_view.py)：添加“保留不支持的命令”设置选项 [`426dbe9`](https://github.com/271374667/NuitkaGUI/commit/426dbe95459321021627adcbdfecafef1164b881)
- ✨ feat(欢迎页面)：添加超链接按钮以跳过设置步骤 [`8186760`](https://github.com/271374667/NuitkaGUI/commit/8186760d48ce93300792cabe89bba5cac98924cc)
- ♻️ refactor(basic_model.py)：在打包失败时处理崩溃报告文件 [`e8527f6`](https://github.com/271374667/NuitkaGUI/commit/e8527f6a0e91a9d54ea796d1ca92c4e2969bc581)
- ♻️ refactor(paths.py)：将nuitka_crash_report.xml文件名中的下划线替换为连字符 [`70ad5db`](https://github.com/271374667/NuitkaGUI/commit/70ad5db8dd76fb3342cade416a6eebd6ffc2fe3d)
- ♻️ refactor(NuitkaGUI.py)：重构编码设置逻辑，确保UTF-8支持 [`e57f39b`](https://github.com/271374667/NuitkaGUI/commit/e57f39beac189743fed6f28ea27768762b38399f)
- ✨ feat(manager_plugin.py, config.py, setting_view.py)：添加自动更新插件功能 [`1f33669`](https://github.com/271374667/NuitkaGUI/commit/1f33669bee3cfeb38ed800a362e9946d772a287e)
- ✨ feat(NuitkaGUI.py, basic_model.py, signal_bus.py)：添加对Nuitka崩溃报告的处理 [`687f15e`](https://github.com/271374667/NuitkaGUI/commit/687f15e4de6a0ec53916e322985aae438974b2b0)
- ♻️ refactor(pip_manager.py, basic_model.py, env_utils.py)：统一代码风格，优化代码可读性 [`8320bef`](https://github.com/271374667/NuitkaGUI/commit/8320bef77f0b9c8f0c6cf6ba39261bde2e8f3759)
- 📝 更新(.gitignore)：添加log.log到忽略列表中 [`5ea6503`](https://github.com/271374667/NuitkaGUI/commit/5ea65031f8296888e57eeaa98f27ae4a9791b634)

## [v0.2.6](https://github.com/271374667/NuitkaGUI/compare/v0.1.0...v0.2.6) - 2024-10-02

- 📝 更新(.gitignore)：添加log.log到忽略列表中 [`aef25b3`](https://github.com/271374667/NuitkaGUI/commit/aef25b3ebb70fc12b769c003433c3e0410c5cbc3)
- 📝 删除(log.log)：移除不再需要的日志文件以减少冗余数据 [`b161533`](https://github.com/271374667/NuitkaGUI/commit/b161533a4fb9b94cb2a8ca0a1f18936710fbfe9f)
- ♻️ refactor(log.log, command.py)：重构CommandBase类，添加WidgetBindMixin混入类 [`1d1ea2d`](https://github.com/271374667/NuitkaGUI/commit/1d1ea2db92ff1e7cab314f3b63f18f65036ff32b)
- ✨ feat(NuitkaGUI)：添加日志记录功能并创建日志文件 [`96dfe62`](https://github.com/271374667/NuitkaGUI/commit/96dfe62ee894d380e63516ac076e97bf8455ec75)

## [v0.1.0](https://github.com/271374667/NuitkaGUI/compare/v0.0.7-alpha...v0.1.0) - 2024-10-02

- ✨ feat(README.md)：更新文档，添加软件功能和使用指南 [`404634d`](https://github.com/271374667/NuitkaGUI/commit/404634d9954ecd7f7f64cb607a78ed605f54a449)
- ✨ feat(pip_manager.py)：重构安装包逻辑以支持多个命令 [`7c8f6bc`](https://github.com/271374667/NuitkaGUI/commit/7c8f6bcfb2d4682f7bdec68311014bde717851c5)
- ✨ feat(NuitkaGUI.py)：将唯一应用标识符更改为"NuitkaGUI" [`49b9a3a`](https://github.com/271374667/NuitkaGUI/commit/49b9a3a2b7840e77758578495b8d9d7917fcb222)
- ✨ feat(pip_manager.py, welcome_model.py, welcome_presenter.py)：添加软件包安装功能 [`06e9d2a`](https://github.com/271374667/NuitkaGUI/commit/06e9d2a5a955932b410805ac3a9325588a434bbb)
- ♻️ refactor(command_choice.py)：重命名类和命令以更好地反映功能 [`f9affa7`](https://github.com/271374667/NuitkaGUI/commit/f9affa718552c50ed5cdf8f1b92c2f094c058daf)
- 🐛 修复(basic_model.py)：在打包过程中记录命令执行结果 [`b259c05`](https://github.com/271374667/NuitkaGUI/commit/b259c0579933037e04fbebac43638064f012f481)
- ✨ feat(NuitkaGUI)：添加窗口对话框工具类以显示警告和信息对话框 [`fba07d3`](https://github.com/271374667/NuitkaGUI/commit/fba07d32185ca10dac89d71765a081a7e4522967)
- ♻️ refactor(NuitkaGUI.py, basic_model.py, basic_presenter.py)：重构代码以优化导入和命令执行 [`5e47e0a`](https://github.com/271374667/NuitkaGUI/commit/5e47e0ad05bc7df376bd780954e9ee98c14ee6fc)
- ♻️ refactor(main_model.py)：使用suppress上下文管理器处理AttributeError [`d83775e`](https://github.com/271374667/NuitkaGUI/commit/d83775e99580d2155500301c3b92eb2bc703dd31)
- ♻️ refactor(config.py)：将可用Python执行文件列表提取为常量 [`172d66a`](https://github.com/271374667/NuitkaGUI/commit/172d66a9451077757c50bcc1b3f3db099064293d)
- ♻️ refactor(command.py)：简化value属性的逻辑，移除路径存在性检查 [`fb3c8db`](https://github.com/271374667/NuitkaGUI/commit/fb3c8dba5f66c9ad9239b888450ffd2bf53a5e1e)
- ⬆️ 升级依赖项：更新pyside6和pyside6-fluent-widgets的版本 [`2d230b3`](https://github.com/271374667/NuitkaGUI/commit/2d230b3a646c7bb2dce541c4301c68f7306f9b39)
- ✨ feat(NuitkaGUI.py)：添加应用程序唯一性检查，防止多次运行 [`3c1a736`](https://github.com/271374667/NuitkaGUI/commit/3c1a736a00999aa5e07ff03b21bcce1262dfd5dc)
- ✨ feat(NuitkaGUI.py)：在主函数中添加QApplication实例化 [`758323c`](https://github.com/271374667/NuitkaGUI/commit/758323c0a9b582d2a4983d2ae495d4f894e6f7b6)
- ✨ feat(.gitignore)：添加对*.xml和*.spec文件的忽略 [`6920f4e`](https://github.com/271374667/NuitkaGUI/commit/6920f4e9318a76828c59842dce497113c499cd69)
- ✨ feat(.gitignore)：添加对*.xml文件的忽略 [`c606590`](https://github.com/271374667/NuitkaGUI/commit/c606590b8976cb53ad9f1211b902ce232213cd84)
- 🐛 fix(command_flag.py)：将disable-ccache命令从"disable-ccache=all"改为"disable-ccache" [`3cb6e9a`](https://github.com/271374667/NuitkaGUI/commit/3cb6e9a5d9541582eb2b55ab52b2e17b36752564)
- ✨ feat(basic_model.py, basic_presenter.py)：为BasicModel添加start方法 [`97c9529`](https://github.com/271374667/NuitkaGUI/commit/97c9529346b86d08b80a80088494f0f092708806)
- ✨ feat(presenter)：添加欢迎页面功能并更新设置视图 [`5444f0f`](https://github.com/271374667/NuitkaGUI/commit/5444f0fbf7e57f69c94ad5195cb8a0b8211f497f)
- ✨ feat(NuitkaGUI.py)：添加欢迎界面以处理首次运行的情况 [`bf5593a`](https://github.com/271374667/NuitkaGUI/commit/bf5593acf39f6e1d575c06ebf289c3f337d46800)
- 📝 更新(.gitignore)：添加对dependence和所有.json文件的忽略规则 [`54c1de6`](https://github.com/271374667/NuitkaGUI/commit/54c1de6844f549c19e4a75c9a6f8de9fe7b029e9)
- ♻️ refactor(dependence_save_path.json)：删除不再使用的依赖保存路径文件 [`0df59f6`](https://github.com/271374667/NuitkaGUI/commit/0df59f64883dccd620b93c02516c51ae01180969)
- ✨ feat(env_manager.py, welcome_model.py, welcome_presenter.py)：添加依赖管理功能 [`f58cba0`](https://github.com/271374667/NuitkaGUI/commit/f58cba07c938dbc11dc57dc9957f9617892c5883)
- ✨ feat(env_manager.py)：添加依赖管理功能以更新系统环境变量 [`3050ed0`](https://github.com/271374667/NuitkaGUI/commit/3050ed023c2a7f54b928e72b96c2dfd146339b29)
- ✨ feat(env_manager.py, welcome_model.py, welcome_presenter.py, python_env_utils.py)：添加Python路径自动检测和手动设置功能 [`649ed4d`](https://github.com/271374667/NuitkaGUI/commit/649ed4dd7c3125b953bd214435be5436479a861b)
- ✨ feat(pip_manager.py)：添加socket连接以测试URL速度 [`b4a3bf4`](https://github.com/271374667/NuitkaGUI/commit/b4a3bf4a58959e8323fcdcb71b8b34d865f19426)
- ✨ feat(welcome_model.py, welcome_presenter.py, welcome_view.py)：重构WelcomeModel以支持pip源管理 [`fc82839`](https://github.com/271374667/NuitkaGUI/commit/fc82839f50d2cfdbcb70625e039e4be0d604fe20)
- ✨ feat(pip_manager.py)：将安装模块列表从硬编码改为配置文件 [`f2b2848`](https://github.com/271374667/NuitkaGUI/commit/f2b2848c2c1f6a6d263f6f5520898f3b3aec37d1)
- ♻️ refactor(tests/test_env_utils.py)：删除不再需要的测试文件 [`47357f7`](https://github.com/271374667/NuitkaGUI/commit/47357f7273900b3cc18ea3e25ebaa20403e4ef26)
- ✨ feat(env_manager.py)：添加EnvManager类以管理环境变量 [`4cd8810`](https://github.com/271374667/NuitkaGUI/commit/4cd8810317820d9620b127f8b8e8e9b223431a26)
- ✨ feat(pip_manager.py)：添加PipManager类以管理Python模块安装 [`d2e0088`](https://github.com/271374667/NuitkaGUI/commit/d2e0088519b2d145bca78d5e4e32e1b6eb1bf43a)
- ✨ feat(ui2py.py)：移除未使用的导入，优化代码结构 [`1c10fe2`](https://github.com/271374667/NuitkaGUI/commit/1c10fe2bd67be2744d4d93837fec013da751a81e)
- ✨ feat(paths.py, env_utils.py)：添加多个依赖文件路径和日志记录功能 [`a459864`](https://github.com/271374667/NuitkaGUI/commit/a459864e0237ac759224ac8e198068aaf931b839)
- ♻️ refactor(main_view.py)：调整导航面板的扩展宽度从100改为150 [`b4f4e11`](https://github.com/271374667/NuitkaGUI/commit/b4f4e11c804fd58bcb038fedc7974854bd05b75a)
- ✨ feat(env_utils.py)：添加获取可写环境变量路径的方法 [`4581b53`](https://github.com/271374667/NuitkaGUI/commit/4581b53edb5746515162ea5f93d2338bf0c2e642)
- ✨ feat(Ui_welcome_page_fluent.py, welcome_view.py, welcome_page_fluent.ui)：重命名按钮并添加新功能 [`f6c1232`](https://github.com/271374667/NuitkaGUI/commit/f6c12325b821e6ce4f5dd220dc04eaa76d8da500)
- ✨ feat(.gitignore)：添加对ruff_cache和dependence目录的忽略 [`9ce0272`](https://github.com/271374667/NuitkaGUI/commit/9ce0272d1e4216121e806e9c70b85174330db59f)
- ✨ feat(setting_model.py, basic_presenter.py, main_presenter.py, setting_presenter.py, signal_bus.py, main_view.py)：添加对Python.exe路径的设置功能 [`5c1012c`](https://github.com/271374667/NuitkaGUI/commit/5c1012cc79eb10c95069d1dc539369fb07f589b7)
- ✨ feat(basic_model.py, basic_presenter.py)：添加项目Python.exe路径的支持 [`226b9a4`](https://github.com/271374667/NuitkaGUI/commit/226b9a4cda91c45cc23989e83d934676652ef88c)
- ✨ feat(presenter)：在BasicPresenter中添加WindowExplorerUtils以查找python.exe [`42f5c93`](https://github.com/271374667/NuitkaGUI/commit/42f5c93e7bbf0538f5ceef595bd56793d0c1b41a)
- ✨ feat(view)：为所有视图添加ToolTipFilter以增强用户体验 [`592af5c`](https://github.com/271374667/NuitkaGUI/commit/592af5c6f5c3063e8c7b042a8ada7b234db9da6c)
- ✨ feat(setting_model.py, setting_presenter.py)：添加重启应用功能 [`0d9cc5b`](https://github.com/271374667/NuitkaGUI/commit/0d9cc5b465f48dacf96288d98e3d59a058d32bcb)
- ✨ feat(env_utils.py)：添加环境变量管理工具类EnvUtils [`2612766`](https://github.com/271374667/NuitkaGUI/commit/2612766b25d57c9cdea98839c80ea07eb5f7685b)
- ♻️ refactor(main_view.py)：移除窗口最大尺寸设置，保持最小尺寸设置 [`3563210`](https://github.com/271374667/NuitkaGUI/commit/356321085b295494ca9c09aebf1e9b0c118fa98c)
- ✨ feat(command_path.py)：添加LOGO_FILE以支持Windows图标功能 [`b5e64b7`](https://github.com/271374667/NuitkaGUI/commit/b5e64b75a3d059e3f8c4eb0739ecade1cd76894c)
- ✨ feat(plugin_presenter.py)：添加插件状态更新功能 [`5532d1c`](https://github.com/271374667/NuitkaGUI/commit/5532d1c79fb0f02a66d1c464d077dea899697e95)
- ✨ feat(config.py, main_model.py, main_presenter.py)：添加优化选项功能 [`2c1d8b7`](https://github.com/271374667/NuitkaGUI/commit/2c1d8b73c7b6813ca19b62b62f2426249954ab7d)
- ♻️ refactor(command_manager.py)：将命令返回格式从逗号分隔改为空格分隔 [`d0d3f0a`](https://github.com/271374667/NuitkaGUI/commit/d0d3f0a58da1400ac16baddf0fbc8a507f836872)
- ✨ feat(plugin): 添加启用插件的命令和相关功能 [`2c83971`](https://github.com/271374667/NuitkaGUI/commit/2c83971ec767d1e68be421ecab47892136061121)
- ♻️ refactor(middleware)：删除不再使用的中间件文件 [`041bae3`](https://github.com/271374667/NuitkaGUI/commit/041bae3d131af4abde9c89fd9fcbe187c9d058f9)
- ✨ feat(command_flag.py)：添加CommandPluginNoDetection类以禁用插件检测 [`727b185`](https://github.com/271374667/NuitkaGUI/commit/727b185efbead32b0469a872be587becea52f874)
- ✨ feat(embed_file_tree.py)：添加最大递归层级限制以防止过度递归 [`494ef3a`](https://github.com/271374667/NuitkaGUI/commit/494ef3a97409ebc95be3a59df7c41667d5daeeff)
- ♻️ refactor(signal_bus.py, command_manager.py, basic_model.py, embed_model.py)：重构命令管理器以支持泛型和命令获取方法 [`8bdd3c0`](https://github.com/271374667/NuitkaGUI/commit/8bdd3c02147575f82d0c6a6337e764dbb392eaae)
- ✨ feat(command_manager.py)：添加对项目和全局Python可执行文件路径的检查 [`296704b`](https://github.com/271374667/NuitkaGUI/commit/296704b0f82da117c25a67184faf98d3059c45e4)
- ✨ feat(command.py, manager_base.py, manager_flag.py)：重构命令管理器以支持通过类型、名称和命令获取命令 [`d97a184`](https://github.com/271374667/NuitkaGUI/commit/d97a184f8ee7f8a92e874c85e37193ca0e854a01)
- ♻️ refactor(command.py)：注释掉单例模式的_instance变量，改用hasattr检查 [`15c572c`](https://github.com/271374667/NuitkaGUI/commit/15c572c34291cab4a3cb4434833041fa7fe2fd3a)
- ✨ feat(config.py, setting_view.py)：在配置中添加优化选项并更新设置视图 [`342e03e`](https://github.com/271374667/NuitkaGUI/commit/342e03e310921541e64cdc5b1b091bc5e11b76f2)
- ✨ feat: 添加设置模块及其视图和呈现器 [`3025d15`](https://github.com/271374667/NuitkaGUI/commit/3025d1510ee2bff201a665b3ebaa3512d002851e)
- ✨ feat(main_view.py)：在MainView中添加插件、参数和设置视图支持 [`4e4e400`](https://github.com/271374667/NuitkaGUI/commit/4e4e400f911a651521b6441f88e863a5db1d652f)
- ✨ feat(config.py, version.py, settings_view.py)：添加项目Python.exe路径配置和设置视图 [`fe09262`](https://github.com/271374667/NuitkaGUI/commit/fe092624a0d2a0a0064e0bd29c3a2c81d63c386c)
- ✨ feat(tran_material2fluent.py)：更新源路径以指向welcome_page.ui [`70e9af6`](https://github.com/271374667/NuitkaGUI/commit/70e9af6000a37c51bebf2c9d88d8fbe0fdfb6c64)
- ✨ feat(args_view.py, args_page_fluent.ui)：添加参数视图和UI文件 [`2e44a2f`](https://github.com/271374667/NuitkaGUI/commit/2e44a2ff0bc052df78107306f34de18d35bb95a3)
- feat(args_page): 转换了参数输出界面 [`e4e6101`](https://github.com/271374667/NuitkaGUI/commit/e4e610126e5c82202eb85a7640e8c70c896fe5ad)
- ✨ feat(main_view.py)：在MainView中添加关于视图的支持 [`b64ea23`](https://github.com/271374667/NuitkaGUI/commit/b64ea2332685751fa0b86ca24f56b34df887fda6)
- ✨ feat(关于页面)：添加关于页面的模型、视图和呈现者 [`491c515`](https://github.com/271374667/NuitkaGUI/commit/491c5157d99556dd5c47b3d257aa679b2889afea)
- ✨ feat(tran_material2fluent.py)：添加对TextPushButton的支持 [`1548cf0`](https://github.com/271374667/NuitkaGUI/commit/1548cf0e88d74322916041530737dcb7a2bf7897)
- feat(interface): 现在所有的ui文件都会格式化以及去除没有使用到的导入 [`9bc200a`](https://github.com/271374667/NuitkaGUI/commit/9bc200ad3eb36f261fb36d9d72ce3b8f086cde10)
- ♻️ refactor(Ui_plugin_page_fluent.py)：重构导入语句以提高可读性 [`21d3336`](https://github.com/271374667/NuitkaGUI/commit/21d33367720b3a31196379f3fd48c28971506565)
- ✨ feat(cmd_text_edit.py, main_view.py)：重构命令文本编辑器并添加主视图 [`bf4991c`](https://github.com/271374667/NuitkaGUI/commit/bf4991c688015e9337d3a9c2674deba40f883f6f)
- ♻️ refactor(command.py)：调整SpinBox的值设置顺序以提高可读性 [`20a144f`](https://github.com/271374667/NuitkaGUI/commit/20a144f5d37c8b2ff38fcca6fe19e62032dbd3cf)
- ✨ feat(command.py)：为CommandBase类添加get_command抽象方法 [`01baa91`](https://github.com/271374667/NuitkaGUI/commit/01baa917cec038fe73786e3b76c53fa6db177fae)
- ♻️ 重构(command_flag.py, command_plugin.py, manager_plugin.py, plugin_model.py)：将插件管理逻辑从CommandPlugin类迁移到ManagerPlugin类，以提高代码的可维护性和可读性。 [`4f4e86d`](https://github.com/271374667/NuitkaGUI/commit/4f4e86d5ba5a90f919f724714272cfff87f13972)
- ♻️ refactor(advanced_view.py)：重构AdvancedView以改进滚动区域布局 [`7352d50`](https://github.com/271374667/NuitkaGUI/commit/7352d5020aed0589442cc857b56123f6f2a0a6d9)
- ✨ feat(command_manager.py)：为命令管理器添加layout_weight属性 [`07aab25`](https://github.com/271374667/NuitkaGUI/commit/07aab254fa6ea09466706955c5efb8f98eebd4fa)
- ✨ feat(nuitka_command)：为多个命令添加中文名称和描述 [`9d5e117`](https://github.com/271374667/NuitkaGUI/commit/9d5e117994b7a772695cb271842356e2e00a0eba)
- ♻️ refactor(nuitka_command)：重构命令管理器以支持可见性过滤 [`9cef254`](https://github.com/271374667/NuitkaGUI/commit/9cef25436d7fd42ed3b91a4de43cfe30a53714e5)
- ✨ feat(command.py)：在CommandBase类中添加value属性 [`437f1ed`](https://github.com/271374667/NuitkaGUI/commit/437f1ed030d9754167c52a83d6131a4aa1377f35)
- ✨ feat(manager): 添加多个管理器类以支持不同命令类型 [`d22bfe7`](https://github.com/271374667/NuitkaGUI/commit/d22bfe7fe2c7e19762faef64d40abed9a5588566)
- ✨ feat(command.py)：实现CommandBase类的单例模式 [`98698ef`](https://github.com/271374667/NuitkaGUI/commit/98698efdf7bb278b7906727d3ae50dc16e4907be)
- ✨ feat(command_choice.py, command_flag.py, command_int.py, command_plugin.py, command_text.py)：为命令类添加中文名称和描述 [`eb0ac3a`](https://github.com/271374667/NuitkaGUI/commit/eb0ac3a1ee036f1a823278b1a4cfd4c2fdab9cef)
- 📝 docs(README.md)：更新项目描述为重写版本说明 [`1920b60`](https://github.com/271374667/NuitkaGUI/commit/1920b60f7616e573700cd2ab9b04da207a052275)
- ✨ feat(nuitka_command)：添加信号总线以更新所有小部件 [`de6a8df`](https://github.com/271374667/NuitkaGUI/commit/de6a8df96b2eb4e67fd968d0e83915c0b5e1f789)
- ✨ feat(nuitka_command)：重构命令管理器以支持插件加载 [`0f3d78b`](https://github.com/271374667/NuitkaGUI/commit/0f3d78b9073e02b3216be58c96c1d3ee69e17ba7)
- ✨ feat(command.py)：重构CommandBase类，添加widget创建和更新方法 [`c4af63a`](https://github.com/271374667/NuitkaGUI/commit/c4af63a4362491508ea7601440817965d75e9800)
- 📝 更新(.gitignore)：添加对.vscode目录的忽略 [`0cc0ab6`](https://github.com/271374667/NuitkaGUI/commit/0cc0ab69abf5b9f6a7afe1a27c19f05564af4b05)
- ✨ feat(nuitka_command)：添加命令管理器和高级视图功能 [`073ac22`](https://github.com/271374667/NuitkaGUI/commit/073ac223caa6a3289927a8a5ba83af54ba61e8b0)
- ✨ feat(nuitka_command)：添加多个命令实现以支持插件和选项 [`800bcca`](https://github.com/271374667/NuitkaGUI/commit/800bcca93f9a08a8382f490c0b52bd512180e6b0)
- Feature: 现在的嵌入式页面在点击选择的时候就会自动将结果传递给command_manager [`3f7b2e4`](https://github.com/271374667/NuitkaGUI/commit/3f7b2e4803c042232057477046f7bfcb12a80951)
- Optimization: 完善了command命令集 [`4806e31`](https://github.com/271374667/NuitkaGUI/commit/4806e316ac1fe36597605a2b0e0861f4aa066c9b)
- Detail: 为嵌入式页面增加了一个新的方法用于将当前的结果写入command_manager中 [`841a680`](https://github.com/271374667/NuitkaGUI/commit/841a680f77ed0eb480200de9541e9e032f1c2562)
- Feature: 实现了basic页面 [`9b3e267`](https://github.com/271374667/NuitkaGUI/commit/9b3e26737fded0004fe35845dcdb6dedbcaf7c3f)
- Feature: 实现了一个拖拽文件的遮罩控件 [`26cab5e`](https://github.com/271374667/NuitkaGUI/commit/26cab5e6bf45131f49e9261965a5d3fc348184c1)
- Feature: 实现了basic_view [`54a2fac`](https://github.com/271374667/NuitkaGUI/commit/54a2fac5a21968fe077c7f11f355a76243c26782)
- Modify: 修改了message_base_view让提示条能够更加简短迅速 [`0015918`](https://github.com/271374667/NuitkaGUI/commit/00159184a5b85400c623e3c8d59db394fb68efce)
- Ui: 现在的树状图控件的右键菜单更加美观 [`dd6b695`](https://github.com/271374667/NuitkaGUI/commit/dd6b69518c56522643af3baf88bce4234cc30e9e)
- Script: 现在的material2fluent脚本能够直接将ui文件复制到项目目录里面 [`a5bedd7`](https://github.com/271374667/NuitkaGUI/commit/a5bedd7378a0509187fde81e354e51665977bbe5)
- Feature: 新增了一个命令行控件，可以重定向所有的输出(目前还未实装) [`306cfd5`](https://github.com/271374667/NuitkaGUI/commit/306cfd5acbccda2a9f46f0407b8ef6cc0d7414e7)
- Ui: 实现了基础页面的Ui设计 [`e1b0c58`](https://github.com/271374667/NuitkaGUI/commit/e1b0c586b0ea9fd9e76fdaa55c34662096d961eb)
- Modify: 现在嵌入式页面获取文件最大文件数的限制降低至500 [`a6ef3a3`](https://github.com/271374667/NuitkaGUI/commit/a6ef3a3395e545ed9f7823a2e2eac44cdfd9f0d7)
- Modify: 修改了嵌入式树状图控件，以及获取命令的形式 [`b8e536d`](https://github.com/271374667/NuitkaGUI/commit/b8e536d0fe5d0e676a124bf1536d80b3726b0ff7)
- Feature: 完整实现了嵌入式页面(包括模型和presenter层) [`4d9c1bb`](https://github.com/271374667/NuitkaGUI/commit/4d9c1bb890c39307cdaa0428fef4e79459a87f50)
- Fix: 修复了thread_utils中run_in_thread类报错的问题 [`1a5ff9a`](https://github.com/271374667/NuitkaGUI/commit/1a5ff9a2f4f3cd3c210ead5fb7d8325f7c6efd65)
- Style: 修改了embed_view中获取加载按钮的名字 [`8984051`](https://github.com/271374667/NuitkaGUI/commit/8984051dbddfc02b735bbc2fa7c0e79786a3f2e3)
- Modify: 修改了视图层基类，使弹窗能够被关闭，同时缩减了时间 [`e2e58e7`](https://github.com/271374667/NuitkaGUI/commit/e2e58e75da9dcc5f9537f9a486731bcf57e9a102)
- Feature: 实现了插件管理类，用于管理所有的插件 [`9304358`](https://github.com/271374667/NuitkaGUI/commit/9304358fa0d5aa67e0c908bfaf788c8c631e1d62)
- Feature: 进一步完善了所有的命令子集 [`a188fc4`](https://github.com/271374667/NuitkaGUI/commit/a188fc4c76e09deae004a162fd2af68e4e37d253)
- Feature: 实现了nuitka命令4大基类 [`3a3e980`](https://github.com/271374667/NuitkaGUI/commit/3a3e98013b269335851dcfcf20ebf7af432da9a9)
- Feature: 创建了用于支持Nuitka命令的基类 [`d62c324`](https://github.com/271374667/NuitkaGUI/commit/d62c3240e8198068ce7532664dd9ce57e21ba8c4)
- Feature: 定义了系统全局设置模块settings [`d9a99ef`](https://github.com/271374667/NuitkaGUI/commit/d9a99efc98e8877cf19940e7edd88794b1119414)
- Feature: 定义了系统核心库core，同时规范了项目路径文件paths [`d18908e`](https://github.com/271374667/NuitkaGUI/commit/d18908e8136a58cf7b2b2c849bd396f493fa4ee2)
- Ui: 实现了欢迎页面的ui [`a47c2c9`](https://github.com/271374667/NuitkaGUI/commit/a47c2c9b60ca16eab89aed9a00a6e4db1222a5c1)
- Resource: 更新了qt的rc资源 [`d8f5661`](https://github.com/271374667/NuitkaGUI/commit/d8f566143e0275788a9bf9a231d89e0bed36041a)
- Feature: 为程序增加了一个配置管理模块 [`04f7d00`](https://github.com/271374667/NuitkaGUI/commit/04f7d007431751029ed954eb78c675f483bfd8fd)
- Feature: 为程序增加了一个信号总线 [`5737a02`](https://github.com/271374667/NuitkaGUI/commit/5737a020604391b2f1e26eb7378380a54997ac23)
- Feature: 完整实现了嵌入式页面 [`f5352a8`](https://github.com/271374667/NuitkaGUI/commit/f5352a8700921291cd2c9b30f90dda49d4acd348)
- Feature: 实现了嵌入式页面的model模型 [`005dc14`](https://github.com/271374667/NuitkaGUI/commit/005dc142512f469044de6293bca0b5ba81e597fc)
- Feature: 实现了嵌入式页面的view视图 [`3e1dd05`](https://github.com/271374667/NuitkaGUI/commit/3e1dd053420372837fd317526204491ea6f0aae6)
- Ui: 实现了嵌入式页面的ui转换为py [`3a0595a`](https://github.com/271374667/NuitkaGUI/commit/3a0595a895af556fdda3a3ad31f75ce9ebc83af2)
- Ui: 实现了嵌入式页面的ui [`f2d3bd6`](https://github.com/271374667/NuitkaGUI/commit/f2d3bd6147553961a3d3183de0b81d9dfeb2a30f)
- Feature: 实现了可以拖拽文件树 [`ee24967`](https://github.com/271374667/NuitkaGUI/commit/ee249679541b74a52552b6b4e8ffd9b81e84564d)
- Style: 格式化了dependence_utils依赖控制工具类 [`3fcbda9`](https://github.com/271374667/NuitkaGUI/commit/3fcbda9458826d0b2f4beb790db97a96e99a77ac)
- Utils: 新增一个调用系统底层的文件资源浏览器工具类 [`ebad0cc`](https://github.com/271374667/NuitkaGUI/commit/ebad0cc50ed5af8ed21d95287206eeea46c7b2f3)
- Utils: 新增一个多线程工具类thread_utils [`8f078c4`](https://github.com/271374667/NuitkaGUI/commit/8f078c4f373aabea1549ef0a1b68094f29dcdae5)
- Utils: 新增一个管理Python环境的工具类python_env_utils [`73149aa`](https://github.com/271374667/NuitkaGUI/commit/73149aa322b9cf963915f31144f8b0d268a32081)
- Utils: 新增一个单例模式工具类 [`35d6a05`](https://github.com/271374667/NuitkaGUI/commit/35d6a05be7890f2b09bd0932979bc510d2ac9a68)
- Feature: 完整实现了插件页面 [`2ce1f04`](https://github.com/271374667/NuitkaGUI/commit/2ce1f04065b0bde133d6d5cc446e3dfd66cbc188)
- Feature: 实现了插件页面的模型 [`b91902b`](https://github.com/271374667/NuitkaGUI/commit/b91902b18aa61dc7c97ee96155d5c958c7e13cc7)
- Feature: 实现了通用页面基类message_base_view [`1b51745`](https://github.com/271374667/NuitkaGUI/commit/1b51745cdc963ce1c07104755cf46a80b8ed5013)
- Feature: 实现了插件页面的view以及控件交互 [`a8898a5`](https://github.com/271374667/NuitkaGUI/commit/a8898a5a95197c320f93f19986cf115c6585dee5)
- Ui: 实现了插件页面的ui的转换 [`ede6ab7`](https://github.com/271374667/NuitkaGUI/commit/ede6ab7932ac84c3fad08075f9eb7c94e64b2d34)
- Ui: 实现了插件页面的ui [`5d550af`](https://github.com/271374667/NuitkaGUI/commit/5d550afe41728b129a1105718c59221d9915c760)
- Script: 更新了一个脚本ui2py，负责将ui转换成py文件 [`46f1d49`](https://github.com/271374667/NuitkaGUI/commit/46f1d4921f291f9c5b560e3546edd58457dc85c7)
- Script: 更新了一个脚本qrc2py，负责将qrc转换成py文件 [`a75ec80`](https://github.com/271374667/NuitkaGUI/commit/a75ec80d847e9946449e20ef5f94b0a7bb5401bc)
- Script: 更新了一个脚本，负责将material的ui转换成fluent的ui [`04b4f1d`](https://github.com/271374667/NuitkaGUI/commit/04b4f1d5e0d94e70e5689695fe44f1f972ea0de3)
- Initialize: 项目初始化 [`96c92fb`](https://github.com/271374667/NuitkaGUI/commit/96c92fb475e37bbbc5ce2773029229b554f842b2)

## [v0.0.7-alpha](https://github.com/271374667/NuitkaGUI/compare/v0.0.6...v0.0.7-alpha) - 2023-10-22

- 修复了README的LOGO错误，调整README文档顺序 [`1fb2b88`](https://github.com/271374667/NuitkaGUI/commit/1fb2b88111124c2308d15ec71477b0ca6647fb42)
- 更新了 README [`89e43a8`](https://github.com/271374667/NuitkaGUI/commit/89e43a8ea41bf7ea6593246658f3062f6c5ab413)
- 更新了 JsonSettings 使其符合 PEP8 规范 [`31af9be`](https://github.com/271374667/NuitkaGUI/commit/31af9be9dc34735aab4f29bedbcfda608f60ce56)
- 第一个可用版本 [`4d6337c`](https://github.com/271374667/NuitkaGUI/commit/4d6337c182338d97410e291e1ce183bc40624b3b)
- 第一个可用版本 [`8c5d011`](https://github.com/271374667/NuitkaGUI/commit/8c5d01121c27c13534ae44a6b5804d55ec1f27f1)
- 界面接近完成 [`856e838`](https://github.com/271374667/NuitkaGUI/commit/856e838eaaa7cc2325ba8780e5d4c053c87176a8)
- 完成了大量更新 [`a6694f0`](https://github.com/271374667/NuitkaGUI/commit/a6694f075d217ec57539ef0f566a6fcf670b7b9e)
- 完成了welcome_page [`5aa03e7`](https://github.com/271374667/NuitkaGUI/commit/5aa03e733e43d3a1420f2b9f55015f1791b41cad)
- 完成了基础页面的view以及主view [`ad2d2d8`](https://github.com/271374667/NuitkaGUI/commit/ad2d2d86e59927f5bbe0a47c149a56efb768b98d)
- 重构1 [`e49f904`](https://github.com/271374667/NuitkaGUI/commit/e49f9040ef12b27318b1c9631456dd6bbc9bcf16)
- 正在重构module [`61dc8af`](https://github.com/271374667/NuitkaGUI/commit/61dc8af4f1607b60b13ea291f514707a0d08704b)
- 一次临时的存档 [`e83257d`](https://github.com/271374667/NuitkaGUI/commit/e83257d4fc25d5bb8e8a6bcff518f15a963b7b3a)
- 一次临时的存档 [`9bc9c75`](https://github.com/271374667/NuitkaGUI/commit/9bc9c75bfb8f7aabefc9205c488aa9efe467e3fc)
- 第一次提交 [`14e1a37`](https://github.com/271374667/NuitkaGUI/commit/14e1a37fac6897fb3925cb2ed3ff6d41fd39b8db)

## [v0.0.6](https://github.com/271374667/NuitkaGUI/compare/v0.0.5...v0.0.6) - 2023-08-06

- 两个分支我终于忍受不住了，实力还是不太够，直接删库换成单分支了 [`fcb487e`](https://github.com/271374667/NuitkaGUI/commit/fcb487e4cb2298d6dc14e1aff893a5d9fe57480b)

## [v0.0.5](https://github.com/271374667/NuitkaGUI/compare/v0.0.5-beta1...v0.0.5) - 2023-07-30

- Squashed commit of the following: [`712036b`](https://github.com/271374667/NuitkaGUI/commit/712036bc9a75b7c3fdb543fc41f28b178d70f575)
- 格式: 更新了README [`312faeb`](https://github.com/271374667/NuitkaGUI/commit/312faeb891db69de413c57b2ce64961fc1dff7d1)
- 修改:版本号错误 [`799c317`](https://github.com/271374667/NuitkaGUI/commit/799c3175971d1703a7a12a54f00295f294653c9a)

## v0.0.5-beta1 - 2023-07-26

### Merged

- 更新项目结构，优化部分代码 [`#1`](https://github.com/271374667/NuitkaGUI/pull/1)

- Squashed commit of the following: [`dc294b6`](https://github.com/271374667/NuitkaGUI/commit/dc294b6be75024b2b689d4c20b99dc13b5815a01)
- style:修改了README中的一些错误 [`f48dfb6`](https://github.com/271374667/NuitkaGUI/commit/f48dfb6c3494c1ba3a9915a787eeff1483fc965b)
- 更新版本号0.0.4 [`7e00e31`](https://github.com/271374667/NuitkaGUI/commit/7e00e316207d1ce4ad114b3962ba5d7c4dec82de)
- Merge BemakeDev branch [`eec0ade`](https://github.com/271374667/NuitkaGUI/commit/eec0adee528dfebf34c9710cb64fefa2b0243ac6)
- 新增了一个.gitignore文件，用于忽略一些不需要提交的文件 [`efb9e92`](https://github.com/271374667/NuitkaGUI/commit/efb9e92f4aeb11aa806a50cad9d53c472453be8d)
- 增强稳定性 [`9b7716f`](https://github.com/271374667/NuitkaGUI/commit/9b7716f2ef5db7d76b95bc01b6e8a103fa7bb8da)
- style: 新的exe [`7946970`](https://github.com/271374667/NuitkaGUI/commit/79469701994056d3e1181f376147a2febb202e94)
- style: 修改了exe的名称 [`1ef859f`](https://github.com/271374667/NuitkaGUI/commit/1ef859f33478c61e67bd409800320f03749513ac)
- 目前可用版本 v0.0.4 [`8518717`](https://github.com/271374667/NuitkaGUI/commit/8518717a5e5de6cde068351d8fd48bfd46965988)
- 新的兼容性打包方式(从网络上获取) [`bcd5cf1`](https://github.com/271374667/NuitkaGUI/commit/bcd5cf164b7f16343a1911bbc8bb760c79ec8dc0)
- 终于可以打包成exe了,同时测试功能进入测试阶段 [`9d053f1`](https://github.com/271374667/NuitkaGUI/commit/9d053f14c6357605344335748dc92321fda338cd)
- 修改:删除了使用python环境的版本，使用固定的python(之后可能会改变) [`906380b`](https://github.com/271374667/NuitkaGUI/commit/906380b1a27990df1f4a01c95144a026909c32c2)
- 优化:对所有耗时项目增加多线程 [`f8052fc`](https://github.com/271374667/NuitkaGUI/commit/f8052fc19a4d3528ae5251fa28f80b6471644b5a)
- new version: 0.0.3 [`b0555e3`](https://github.com/271374667/NuitkaGUI/commit/b0555e3c5fab4a357e88b008b5490f5652a898e5)
- update [`06d202b`](https://github.com/271374667/NuitkaGUI/commit/06d202babbe0829e205c87741063b3d26c9ef5dd)
- New File: 新增了README.md [`67529cf`](https://github.com/271374667/NuitkaGUI/commit/67529cfd9848b66c94c513196818783b0797ecc1)
- New Version 0.1.0 [`e846dc3`](https://github.com/271374667/NuitkaGUI/commit/e846dc3238b8296b02ad0a0e825a5d821f2de010)
