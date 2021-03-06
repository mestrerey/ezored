// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from proj.djinni

#pragma once

#include "djinni_support.hpp"
#include "ezored/helpers/CustomerHelper.hpp"

namespace djinni_generated {

class EZRHelperCustomerHelper final : ::djinni::JniInterface<::ezored::helpers::CustomerHelper, EZRHelperCustomerHelper> {
public:
    using CppType = std::shared_ptr<::ezored::helpers::CustomerHelper>;
    using CppOptType = std::shared_ptr<::ezored::helpers::CustomerHelper>;
    using JniType = jobject;

    using Boxed = EZRHelperCustomerHelper;

    ~EZRHelperCustomerHelper();

    static CppType toCpp(JNIEnv* jniEnv, JniType j) { return ::djinni::JniClass<EZRHelperCustomerHelper>::get()._fromJava(jniEnv, j); }
    static ::djinni::LocalRef<JniType> fromCppOpt(JNIEnv* jniEnv, const CppOptType& c) { return {jniEnv, ::djinni::JniClass<EZRHelperCustomerHelper>::get()._toJava(jniEnv, c)}; }
    static ::djinni::LocalRef<JniType> fromCpp(JNIEnv* jniEnv, const CppType& c) { return fromCppOpt(jniEnv, c); }

private:
    EZRHelperCustomerHelper();
    friend ::djinni::JniClass<EZRHelperCustomerHelper>;
    friend ::djinni::JniInterface<::ezored::helpers::CustomerHelper, EZRHelperCustomerHelper>;

};

}  // namespace djinni_generated
