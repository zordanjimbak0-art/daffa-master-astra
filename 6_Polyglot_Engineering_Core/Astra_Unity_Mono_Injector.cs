using System;
using System.IO;
using System.Text;
using System.Reflection;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace AstraUnityMonoCore
{
    public sealed class MonoRuntimeController
    {
        private static readonly byte[] XorKey = Encoding.ASCII.GetBytes("sdhfioshdio@#%#@%@$@dgfi!~@$#joash");

        public static string DecryptXorSavePayload(byte[] encryptedBytes)
        {
            if (encryptedBytes == null || encryptedBytes.Length == 0)
                return string.Empty;

            byte[] output = new byte[encryptedBytes.Length];
            for (int i = 0; i < encryptedBytes.Length; i++)
            {
                output[i] = (byte)(encryptedBytes[i] ^ XorKey[i % XorKey.Length]);
            }
            return Encoding.UTF8.GetString(output);
        }

        public static byte[] EncryptXorSavePayload(string jsonPayload)
        {
            byte[] raw = Encoding.UTF8.GetBytes(jsonPayload);
            byte[] output = new byte[raw.Length];
            for (int i = 0; i < raw.Length; i++)
            {
                output[i] = (byte)(raw[i] ^ XorKey[i % XorKey.Length]);
            }
            return output;
        }

        public static bool SetStaticFieldValue(string typeName, string fieldName, object newValue)
        {
            foreach (Assembly asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                Type targetType = asm.GetType(typeName, false, true);
                if (targetType != null)
                {
                    FieldInfo field = targetType.GetField(fieldName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                    if (field != null)
                    {
                        field.SetValue(null, newValue);
                        return true;
                    }
                }
            }
            return false;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #01] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_01
{
    public class SingletonReflector_01
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #02] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_02
{
    public class SingletonReflector_02
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #03] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_03
{
    public class SingletonReflector_03
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #04] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_04
{
    public class SingletonReflector_04
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #05] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_05
{
    public class SingletonReflector_05
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #06] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_06
{
    public class SingletonReflector_06
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #07] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_07
{
    public class SingletonReflector_07
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #08] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_08
{
    public class SingletonReflector_08
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #09] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_09
{
    public class SingletonReflector_09
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #10] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_10
{
    public class SingletonReflector_10
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #11] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_11
{
    public class SingletonReflector_11
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #12] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_12
{
    public class SingletonReflector_12
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #13] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_13
{
    public class SingletonReflector_13
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #14] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_14
{
    public class SingletonReflector_14
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #15] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_15
{
    public class SingletonReflector_15
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #16] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_16
{
    public class SingletonReflector_16
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #17] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_17
{
    public class SingletonReflector_17
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #18] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_18
{
    public class SingletonReflector_18
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #19] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_19
{
    public class SingletonReflector_19
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #20] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_20
{
    public class SingletonReflector_20
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #21] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_21
{
    public class SingletonReflector_21
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #22] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_22
{
    public class SingletonReflector_22
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #23] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_23
{
    public class SingletonReflector_23
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #24] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_24
{
    public class SingletonReflector_24
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #25] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_25
{
    public class SingletonReflector_25
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}

// ============================================================================
// [C# .NET SUBSYSTEM #26] Unity Assembly-CSharp Reflection Scanner & Singleton Hook
// Purpose: Locates active MonoBehaviour singletons (Wallet, AnimalManager, Inventory) and mutates fields safely.
// Hardware Target: AMD Ryzen 5 5600 | Radeon RX 580 (4GB VRAM) | 16GB DDR4
// ============================================================================
namespace AstraMonoSubsystem_26
{
    public class SingletonReflector_26
    {
        public static object InvokeSingletonMethod(string className, string instanceProp, string methodName, object[] args)
        {
            foreach (var asm in AppDomain.CurrentDomain.GetAssemblies())
            {
                var type = asm.GetType(className, false, true);
                if (type == null) continue;
                var prop = type.GetProperty(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                var field = type.GetField(instanceProp, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
                object instance = prop != null ? prop.GetValue(null, null) : (field != null ? field.GetValue(null) : null);
                if (instance == null) continue;
                var method = type.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                if (method != null)
                {
                    return method.Invoke(instance, args);
                }
            }
            return null;
        }
    }
}
