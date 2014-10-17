/** @jsx React.DOM */

var ImageBundle = React.createClass({
    mixins: [CheckboxMixin],
    getInitialState: function(){
        this.props.item.state.checked = false;
        return this.props.item.state;
    },
    handleClick: function(){
        this.props.setFocus(this);
    },
    render: function() {
        var className = 'type-image' + (this.props.focused ? ' focused' : '');
        var checkbox = this.props.canEdit ? <input type="checkbox" className="ws-checkbox" onChange={this.handleCheck} checked={this.state.checked} /> : null;

        var src= "data:image/png;base64," + this.state.interpreted
        return(
            <div className="ws-item" onClick={this.handleClick}>
                {checkbox}
                <div className={className} ref={this.props.item.state.ref}>
                    <img src={src} />
                </div>
            </div>
        );
    } // end of render function
}); //end of  ContentsBundle
