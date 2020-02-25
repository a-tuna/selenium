#coding=utf-8
import jpype
jvmpath = jpype.get_default_jvm_path()
jpype.startJVM(jvmpath)
jpype.java.lang.System.out.println("hello world!")
jpype.shutdownJVM()