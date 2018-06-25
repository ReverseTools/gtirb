#include <gtest/gtest.h>
#include <gtirb/CFGSet.hpp>
#include <gtirb/Module.hpp>
#include <memory>

TEST(Unit_CFGSet, ctor_0)
{
    EXPECT_NO_THROW(gtirb::CFGSet());
}

TEST(Unit_CFGSet, getCFG_EA)
{
    gtirb::EA ea{22678};
    auto node = std::make_unique<gtirb::CFGSet>();
    EXPECT_NO_THROW(node->getCFG(ea));
    EXPECT_TRUE(node->empty());
    EXPECT_EQ(size_t{0}, node->size());

    auto child = node->getCFG(ea);
    EXPECT_TRUE(child == nullptr);
    EXPECT_TRUE(node->empty());
    EXPECT_EQ(size_t{0}, node->size());

    child = node->createCFG(ea);
    EXPECT_TRUE(child != nullptr);
    EXPECT_FALSE(node->empty());
    EXPECT_EQ(size_t{1}, node->size());

    child = node->getCFG(ea);
    EXPECT_TRUE(child != nullptr);
    EXPECT_FALSE(node->empty());
    EXPECT_EQ(size_t{1}, node->size());

    // Make sure we don't create it again.
    child = node->createCFG(ea);
    EXPECT_TRUE(child != nullptr);
    EXPECT_FALSE(node->empty());
    EXPECT_EQ(size_t{1}, node->size());
}

TEST(Unit_CFGSet, getCFG_ProcedureName)
{
    const gtirb::EA ea{22678};
    const std::string procedureName{"Foo"};

    auto node = std::make_unique<gtirb::CFGSet>();
    EXPECT_NO_THROW(node->getCFG(ea));
    EXPECT_TRUE(node->empty());
    EXPECT_EQ(size_t{0}, node->size());

    child = node->createCFG(ea);
    EXPECT_TRUE(child != nullptr);
    EXPECT_FALSE(node->empty());
    EXPECT_EQ(size_t{1}, node->size());
    EXPECT_NO_THROW(child->setProcedureName(procedureName));

    child = node->getCFG(procedureName);
    EXPECT_TRUE(child != nullptr);
    EXPECT_FALSE(node->empty());
    EXPECT_EQ(size_t{1}, node->size());
}

TEST(Unit_CFGSet, getCFG_invalid)
{
    gtirb::EA ea{};
    auto node = std::make_unique<gtirb::CFGSet>();
    EXPECT_NO_THROW(node->getCFG(ea));
}