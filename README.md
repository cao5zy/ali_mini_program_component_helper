# ali_mini_program_component_helper
这是一个开发支付宝小程序组件的帮助程序。

假设你打算开发一个名为`items`的template并且你已经在`~/app/your_program`下配置好了整个支付宝小程序的开发环境。
运行如下命令，只将`items`复制到`~/app/your_program_items`文件夹下。
```
ali_mini_helper develop --project ~/app/your_program --template items
```
接下来你要做的是在`~/app/your_program_items`下完成开发和调试，然后在运行如下命令，将`items`代码拷贝回`~/ap/your_program`。
```
ali_mini_helper finish --project ~/app/your_program --template items
```
执行的开始阶段，程序会检查`~/app/your_program`下的git状态，只有当状态是clearn是，该命令才会继续执行。命令命令执行成功后，`~/app/your_program_items`会被删除。
