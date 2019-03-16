// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from proj.djinni

#pragma once

#include "ezored/net/http/HttpHeader.hpp"
#include "ezored/net/http/HttpMethod.hpp"
#include "ezored/net/http/HttpRequestParam.hpp"
#include <string>
#include <utility>
#include <vector>

namespace ezored { namespace net { namespace http {

struct HttpRequest final {
    std::string url;
    HttpMethod method;
    std::vector<HttpRequestParam> params;
    std::vector<HttpHeader> headers;
    std::string body;

    HttpRequest(std::string url_,
                HttpMethod method_,
                std::vector<HttpRequestParam> params_,
                std::vector<HttpHeader> headers_,
                std::string body_)
    : url(std::move(url_))
    , method(std::move(method_))
    , params(std::move(params_))
    , headers(std::move(headers_))
    , body(std::move(body_))
    {}
};

} } }  // namespace ezored::net::http