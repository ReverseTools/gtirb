#pragma once

#include <gtirb/EA.hpp>
#include <gtirb/Node.hpp>
#include <memory>
#include <vector>

namespace gtirb
{
    class CFG;

    ///
    /// \class CFGSet
    /// \author John E. Farrier
    ///
    /// Storage for all gtirb::CFG objects for a single gtirb::Module.
    /// This has gtirb::CFG children.
    ///
    /// \todo Remove.  Instead we just want to use the ICFG graph data
    /// structure.
    ///
    class GTIRB_GTIRB_EXPORT_API CFGSet : public Node
    {
    public:
        CFGSet();
        CFGSet(const CFGSet& other) = delete;
        CFGSet& operator=(const CFGSet& rhs) = delete;

        ///
        /// Defaulted trivial destructor.
        ///
        ~CFGSet() override;

        ///
        /// Get the CFG at the given EA.
        ///
        /// \param x    The EA of the gtirb::CFG to get.
        /// \return     The CFG at the given EA or nullptr.
        ///
        CFG* getCFG(gtirb::EA x) const;

        ///
        /// Get the CFG with the given Procedure Name
        ///
        /// \param x    The procedure name of the gtirb::CFG to get.
        /// \return     The CFG at the given EA or nullptr.
        ///
        /// \sa CFG::getProcedureName()
        ///
        CFG* getCFG(const std::string& x) const;

        ///
        /// Create the CFG at the given EA.
        ///
        /// This is preferable to adding CFGs manually as it ensures no duplicate CFGs are
        /// created.
        ///
        /// \pre No CFG currently exists at the given EA.
        ///
        /// \param x    The EA of the gtirb::CFG to get (or create).
        /// \return     The CFG at the given EA.
        ///
        CFG* createCFG(gtirb::EA x);

        const std::vector<std::unique_ptr<CFG>>& getCFGs() const;

        ///
        /// Serialization support.
        ///
        template <class Archive>
        void serialize(Archive& ar, const unsigned int /*version*/);

    private:
        std::vector<std::unique_ptr<CFG>> contents;
    };
}

BOOST_CLASS_EXPORT_KEY(gtirb::CFGSet);